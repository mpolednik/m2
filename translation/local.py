# coding=utf-8
NAME=u'Název'
TEXT=u'Popis'
CONTENT=u'Obsah'
LINK=u'Odkaz'
FILE=u'Soubor'

BACKTOTOP=u'Zpět nahoru'
LOADING=u'Načítám další příspěvky...'
LOADING_FINISHED=u'Všechny příspěvky načteny!'

ALL=u'Vše'
ACTIONS=u'Akce'
SEND=u'Odeslat'
BACK=u'Zpět'

category = {
    'INVALID_NAME': u'Délka názvu kategorie musí být mezi %(min)d a %(max)d znaky!',
    'INVALID_TEXT': u'Maximální délka textu je %(max)d znaků!',
    'EDITTED': u'Kategorie editována.',
    'CREATED': u'Kategorie vytvořena.',
    'CREATE': u'Vytvořit',
    'EDIT': u'Editovat',
    'REQUEST_NEW': u'Zažádat o novou kategorií',
    'REQUEST_MOD': u'Zažádat o post moderátora',
    'CREATE_NEW': u'Založit novou kategorií',

    'TITLE_NEW': u'nová kategorie',
    'TITLE_ALL': u'všechny kategorie',
    'TITLE_SUBMIT': u'vložení obrázku',
    'TITLE_EDIT': u'editace kategorie',

    'TITLE_ADMIN_LIST': u'seznam kategorií',
}

category_submit = {
    'INVALID_IMAGE': u'Špatný formát obrázku, je to vůbec obrázek?',
    'INVALID_NAME': u'Délka názvu obrázku musí být mezi %(min)d a %(max)d znaky!',
    'INVALID_TEXT': u'Maximální délka textu je %(max)d znaků!',
    'INVALID_LINK': u'Maximální délka odkazu je %(max)d znaků!',
    'IMAGE_POSTED': u'Obrázek nahrán a zobrazen!',
    'POST': u'Vložit',
}

user = {
    'MAIL': u'E-mailová adresa',
    'PASS': u'Heslo',
    'NICK': u'Přezdívka',
    'PHONE': u'Telefonní číslo',

    'INVALID_MAIL': u'Neplatná e-mailový adresa! E-mail musí být zadán ve formátu name@domain.tld.',
    'INVALID_PASS': u'Heslo musí mít minimálně %(min)d znaky!',
    'INVALID_NAME': u'Délka přezdívky musí být mezi %(min)d a %(max)d znaky!',
    'EXISTS_MAIL': u'Tato e-mailová adresa je již zaregistrována!',
    'EXISTS_NAME': u'Tato přezdívka je již zaregistrována!',
    'EDITTED': u'Uživatelské nastavení změněno.',
    'NOT_EDITTED': u'Uživatelské nastavení se nepovedlo změnit.',
    'LOGGED_IN': u'Přihlášen. Nepropadejte panice!',
    'LOGGED_OUT': u'Odhlášen. Možná.',
    'LOGIN': u'přihlášení',
    'LOGOUT': u'odhlášení',
    'REGISTER': u'registrace',
    'NOT_LOGGED_IN': u'Přihlášení se nezdařilo.',
    'REGISTERED': u'Registrace a přihlášení v pořádku. Vítejte!',
    'NOT_REGISTERED': u'Registrace se nezdařila.',
    'EDIT': u'Editovat',

    'TITLE_LOGIN': u'přihlášení',
    'TITLE_REGISTER': u'registrace',

    'TITLE_ADMIN_LIST': u'seznam uživatelů',
}

comment = {
    'INVALID_TEXT': u'Délka obsahu musí být mezi %(min)d a %(max)d znaky!',
    'ALREADY_COMMENTED': u'Komentář nejvyšší úrovně můžete mít jen jeden.',
    'POSTED': u'Komentář uložen.',
    'DELETED': u'Komentář smazán.',
    'EDITED': u'Komentář editován.',
    'VOTED': u'Hodnoceno!',
    'REPLY': u'Odpovědět',

    'TITLE_ONE': u'komentář',
    'TITLE_EDIT': u'editace komentáře',

    'TITLE_ADMIN_LIST': u'seznam komentářů',
}

image = {
    'DELETED': u'Obrázek smazán.',
    'EDITED': u'Obrázek editován.',
    'VOTED': u'Hodnoceno!',
    'EXIF': u'EXIF data',
    'COMMENT': u'Komentovat',
    'COMMENTS': u'Komentáře',
    'INFO': u'Informace',
    'REPLIED': u'Napsáno',

    'TITLE_EDIT': u'editace obrázku',

    'TITLE_ADMIN_LIST': u'seznam obrázků',
}

search = {
    'HINT_SEARCH': u'Hledat...',
    'CATEGORIES': u'Kategorie',
    'USERS': u'Uživatelé',
    'IMAGES': u'Obrázky',

    'TITLE_SEARCH': u'vyhledávání',
}

adminmenu = {
    'REQUESTS': u'Požadavky',
    'STATISTICS': u'Statistika',
    'CATEGORIES': u'Kategorie',
    'USERS': u'Uživatelé',
    'IMAGES': u'Obrázky',
    'COMMENTS': u'Komentáře',
}

admin = {
    'REQUEST': u'Požadavek',
    'SEND_TOKEN': u'Poslat SMS s jednorázovým přihlašovacím kódem',
    'KEY_SENT': u'Přihlašovací kód byl odeslán',
    'KEY_NOT_SENT': u'Nepovedlo se odeslat přihlašovací kód :(',
    'PHONE_NOT_SET': u'Pro administrátorské přihlášení si musíte nastavit telefonní číslo!',
    'TOKEN': u'Přihlašovací kód',
    'LOGGED_IN': u'Přihlášen. Nepropadejte panice!',
    'NOT_LOGGED_IN': u'Přihlášení se nezdařilo.',
    'LOGIN': u'Přihlásit',
    'SMS_TEXT': u'Vas jednorazovy prihlasovaci kod je {} (platnost 2 minuty).',
    'SUPERLOGIN': u'Zapnout administraci',
    'SUPERLOGOUT': u'Vypnout administraci',
    'ADMIN': u'Administrátor',
    'MOD': u'Moderátor',
    'NOTICE': u'Po aktivaci administrace získáte další práva...',

    'TITLE_LOGIN': u'administrátorské přihlášení',
}

statistics = {
    'GENERATED': u'Vygenerováno',

    'TITLE': u'statistika',
}

actions = {
    'NEW_IMAGE': u'Vložit obrázek',
    'BECOME_MOD': u'Stát se moderátorem',
    'PASS_MOD': u'Vzdát se moderátorství',
    'EDIT': u'Upravit',
    'DELETE': u'Smazat',
    'ACCEPT': u'Schválit',
    'DECLINE': u'Zamítnout',
    'REQUEST_CATEGORY': u'Zažádat o kategorií',
    'REQUEST_MOD': u'Zažádat o moderátorství',
    'UPVOTE': u'Líbí se mi',
    'DOWNVOTE': u'Nelíbí se mi',
}

request = {
    'INVALID_NAME': u'Délka názvu požadavku musí být mezi %(min)d a %(max)d znaky!',
    'INVALID_TEXT': u'Maximální délka textu je %(max)d znaků!',
    'OK': u'Požadavek odeslán.',
    'FAIL': u'Požadavek se nepodařilo odeslat',
    'ACCEPTED': u'Požadavek schválen.',
    'DECLINED': u'Požadavek zamítnut.',
    'MOD_REQUESTED': u'O moderátorství v této kategorií jste již zažádal!',

    'TITLE_LIST': u'seznam požadavků',
    'TITLE_REQUEST': u'nový požadavek',
    'TITLE_DETAILS': u'podrobnosti požadavku',
    'TITLE_NEW': u'nový požadavek',
}

sms = {
    'STATE': u'Stav',
    'STATE_UNKNOWN': u'neznámý',
    'STATE_UNPROCESSED': u'příprava ke spracování',
    'STATE_PROCESSED': u'zpracováno',
    'STATE_SENT': u'odesláno',
    'STATE_ERROR': u'došlo k chybě',
}
