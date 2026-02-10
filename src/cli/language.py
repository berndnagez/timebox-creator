import gettext


def set_language(lang):
    locales_dir = 'locales'
    translation = gettext.translation(
        'messages', localedir=locales_dir, languages=[lang])
    translation.install()
