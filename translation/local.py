# coding=utf-8
NAME=u'Jméno'
TEXT=u'Popis'
LINK=u'Odkaz'
IMAGE=u'Obrázek'
PASS=u'Heslo'
MAIL=u'E-mail'
UNAME=u'Přezdívka'
PHONE=u'Telefonní číslo'
CONTENT=u'Obsah'
ACCOUNT=u'Účet'
LOGOUT=u'Odhlásit se'
LOGIN=u'Přihlásit se'
SUPERLOGIN=u'Zapnout administraci'
SUPERLOGOUT=u'Vypnout administraci'
REGISTER=u'Registrace'
ALL=u'Vše'
ADMIN=u'Administrátor'
MOD=u'Moderátor'
ACTIONS=u'Akce'
SEND=u'Odeslat'

category = {
    'NEW': u'Nová kategorie',
    'INVALID_NAME': u'Délka názvu kategorie musí být mezi %(min)d a %(max)d znaky!',
    'INVALID_TEXT': u'Maximální délka textu je %(max)d znaků!',
    'EDITTED': u'Kategorie editována.',
    'CREATED': u'Kategorie vytvořena.',
    'CREATE': u'Vytvořit',
    'EDIT': u'Editovat',
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
    'INVALID_MAIL': u'Neplatná e-mailový adresa! E-mail musí být zadán ve formátu name@domain.tld.',
    'INVALID_PASS': u'Heslo musí mít minimálně %(min)d znaky!',
    'INVALID_NAME': u'Délka přezdívky musí být mezi %(min)d a %(max)d znaky!',
    'EXISTS_MAIL': u'Tato e-mailová adresa je již zaregistrována!',
    'EXISTS_NAME': u'Tato přezdívka je již zaregistrována!',
    'EDITTED': u'Uživatelské nastavení změněno.',
    'NOT_EDITTED': u'Uživatelské nastavení se nepovedlo změnit.',
    'LOGIN': u'Přihlášen. Nepropadejte panice!',
    'LOGOUT': u'Odhlášen. Možná.',
    'NOT_LOGIN': u'Přihlášení se nezdařilo.',
    'REGISTERED': u'Registrace a přihlášení v pořádku. Vítejte!',
    'NOT_REGISTERED': u'Registrace se nezdařila.',
    'EDIT': u'Editovat',
}

comment = {
    'INVALID_TEXT': u'Délka obsahu musí být mezi %(min)d a %(max)d znaky!',
    'ALREADY_COMMENTED': u'Komentář nejvyšší úrovně můžete mít jen jeden.',
    'POSTED': u'Komentář uložen.',
    'DELETED': u'Komentář smazán.',
    'EDITED': u'Komentář editován.',
    'VOTED': u'Hodnoceno!',
    'REPLY': u'Odpovědět',
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
}

search = {
    'HINT_SEARCH': u'Hledat...',
    'SEARCH': u'Vyhledávání',
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
    'TOKEN': u'Přihlašovací kód',
    'LOGGED_IN': u'Přihlášen. Nepropadejte panice!',
    'NOT_LOGGED_IN': u'Přihlášení se nezdařilo.',
    'LOGIN': u'Přihlásit',
    'SMS_TEXT': u'Vas jednorazovy prihlasovaci kod je {} (platnost 2 minuty).',
}

statistics = {
    'GENERATED': u'Vygenerováno',
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
