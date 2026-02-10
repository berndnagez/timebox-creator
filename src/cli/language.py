import gettext
import json


def set_language(conf_file_path: str):
    language = get_language(conf_file_path)
    locales_dir = 'locales'
    translation = gettext.translation(
        'messages', localedir=locales_dir, languages=[language])
    translation.install()


def get_saved_language(conf_file_path: str) -> str:
    with open(conf_file_path, 'r') as file:
        language = json.load(file)
    return language['language']


def get_input_language():
    pass


def save_language():
    pass


def get_language(conf_file_path: str):
    language = get_saved_language(conf_file_path)
    return language
