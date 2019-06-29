# yandex-translation-to-tinycards
Allows you to see translation of different words or phrases using Yandex api and add them to TinyCards by Duolingo automatically.

It has console interface only.

## Installation
Guaranteed to work in Unix with python >3.

1. Set environment variables:
    * 'YANDEX_TRNLS_API_KEY' - (https://translate.yandex.com/developers/keys)
    * 'YANDEX_DICT_API_KEY' - (https://yandex.ru/dev/keys/get/?service=dict)
    * 'TC_LOGIN' - Login for TinyCards service (https://tinycards.duolingo.com)
    * 'TC_PASSWORD' - Password for TinyCards service
    * 'TC_CURRENT_DECK' - The name of the deck where cards will be saved in TinyCards service (can be changed during the program)

    You can set them in ~/.bashrc or ~/.zshrc with `export 'NAME'='VALUE'`.
2. Navigate to downloaded repository and install all dependencies by command `pip install -r requirements.txt`

## Usage

`python translate.py [words to translate]`
    You can pass additional arguments (if you want) to automatically transfer to translation stage without prompting to input phrase or word to translate
