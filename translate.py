import sys
import os
import json

import requests

import tinycards_service as tc

trnsl_api_key = os.environ['YANDEX_TRNLS_API_KEY']
dict_api_key = os.environ['YANDEX_DICT_API_KEY']

def detect_language(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/detect'

    params = {
        'key': trnsl_api_key,
        'text': text,
        'hints': 'en, ru'
    }

    r = requests.get(url, params=params)

    if r.status_code == 200:
        return r.json()['lang']
    else:
        return 'en'

def parse_translations(tr_objects):
    output = []

    for tr_object in tr_objects:
        trs = tr_object['tr']
        for tr in trs:
            output.append(tr['text'])

    return output

def get_translations(text):
    is_dict_transl = len(text.split()) == 1
    url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup' if is_dict_transl \
        else 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    avail_langs = ['en', 'ru']
    from_lang = detect_language(text)
    to_lang = [l for l in avail_langs if l != from_lang][0]

    params = {
        'key': dict_api_key if is_dict_transl else trnsl_api_key,
        'text': text,
        'lang': detect_language(text) + '-' + to_lang
    }

    r = requests.get(url, params=params)

    if r.status_code == 200:
        if is_dict_transl:
            return parse_translations(r.json()['def'])
        else:
            return r.json()['text']
    else:
        return {'errorCode': r.status_code}

def main(argv):
    print(f"Current deck: {os.environ['TC_CURRENT_DECK']}")

    while True:
        if len(argv) > 0:
            front = ' '.join(argv)
            argv.clear()
        else:
            front = input("Input word or phrase to translate ('e' - exit): ")
            if front == 'e':
                print('Exiting...')
                sys.exit()

        trans_list = get_translations(front)
        for i in range(len(trans_list)):
            print(i, trans_list[i])

        while True:
            i = input("Choose translation num ('e' - exit, 'd' - current deck, 'cd' - change deck): ")

            if i == 'e':
                print('Exiting...')
                sys.exit()
            elif i == 'd':
                print(os.environ['TC_CURRENT_DECK'])
                continue
            elif i == 'cd':
                deck_name = input('Input decks name: ')
                os.environ['TC_CURRENT_DECK'] = deck_name
                continue

            try:
                i = int(i)
                assert i in range(len(trans_list))
            except ValueError:
                print('Error occured. Repeat please...')
                continue

            back = trans_list[i]
            break

        tc.add((front, back))


if __name__ == "__main__":
   main(sys.argv[1:])