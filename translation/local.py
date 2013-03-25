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
NOTFOUND=u'Požadovaná stránka neexistuje!'
EXCEPTION=u'Na stránce došlo k chybě!'
SECURITYEXCEPTION=u'Pro tuto akci nemáte dostatečné oprávnění!'

category = {
    'INVALID_NAME': u'Délka názvu kategorie musí být mezi %(min)d a %(max)d znaky!',
    'INVALID_TEXT': u'Maximální délka textu je %(max)d znaků!',
    'EDITED': u'Kategorie editována.',
    'CREATED': u'Kategorie vytvořena.',
    'CREATE': u'Vytvořit',
    'EDIT': u'Editovat',
    'REQUEST_NEW': u'Zažádat o novou kategorií',
    'REQUEST_MOD': u'Zažádat o post moderátora',
    'CREATE_NEW': u'Založit novou kategorií',
    'MODERATORS': u'Moderátoři',
    'NONEXISTANT': u'<neexistující kategorie>',

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
    'NONEXISTANT': u'<neexistující uživatel>',
    'SETTINGS': u'nastavení',

    'SCORE_IMAGES': u'Skóre obrázků',
    'SCORE_COMMENTS': u'Skóre komentářů',
    'NUM_IMAGES': u'Obrázků',
    'NUM_COMMENTS': u'Komentářů',
    'CREATED': u'Vytvořen',
    'MODERATES': u'Moderuje',

    'ADMINISTRATOR': u'administrátor',
    'MODERATOR': u'moderátor',
    'USER': u'uživatel',

    'INVALID_MAIL': u'Neplatná e-mailový adresa! E-mail musí být zadán ve formátu name@domain.tld.',
    'INVALID_PASS': u'Heslo musí mít minimálně %(min)d znaky!',
    'INVALID_NAME': u'Délka přezdívky musí být mezi %(min)d a %(max)d znaky!',
    'INVALID_NAME_CHARS': u'Přezdívka musí obsahovat pouze písmena, číslice a znaky _ a -',
    'EXISTS_MAIL': u'Tato e-mailová adresa je již zaregistrována!',
    'EXISTS_NAME': u'Tato přezdívka je již zaregistrována!',
    'EDITED': u'Uživatelské nastavení změněno.',
    'NOT_EDITED': u'Uživatelské nastavení se nepovedlo změnit.',
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
    'EDITED': u'Komentář editován.',
    'REPLY': u'Odpovědět',
    'EDIT': u'Editovat',
    'DELETED': u'Smazaný komentář.',
    'STATE_DELETED': u'smazán',
    'STATE_HEALTHY': u'aktivní',

    'TITLE_ONE': u'komentář',
    'TITLE_EDIT': u'editace komentáře',

    'TITLE_ADMIN_LIST': u'seznam komentářů',
}

image = {
    'DELETED': u'Obrázek smazán.',
    'EDITED': u'Obrázek editován.',
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

confirms = {
    'COMMENT_DELETE': u'Opravdu chcete smazat komentář "{}"?',
    'CATEGORY_DELETE': u'Opravdu chcete smazat kategorií "{}"?',
    'USER_DELETE': u'Opravdu chcete smazat uživatele "{}"?',
    'USER_PROMOTE': u'Opravdu chcete uživateli "{}" darovat administrační práva?',
    'USER_DEMOTE': u'Opravdu chcete uživateli "{}" zrušit administrační práva?',
    'IMAGE_DELETE': u'Opravdu chcete smazat obrázek "{}"?',
    'REQUEST_DELETE': u'Opravdu chcete smazat požadavek "{}"?',
    'REQUEST_DECLINE': u'Opravdu chcete zamítnout požadavek "{}"?',
    'REQUEST_ACCEPT': u'Opravdu chcete schválit požadavek "{}"?',
}

admin = {
    'CATEGORY_DELETED': u'Kategorie smazána!',
    'COMMENT_DELETED': u'Komentář smazán!',
    'REQUEST_DELETED': u'Požadavek smazán!',
    'USER_DELETED': u'Uživatel smazán!',

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
    'SUPERLOGIN': u'zapnout administraci',
    'SUPERLOGOUT': u'vypnout administraci',
    'ADMIN': u'Administrátor',
    'MOD': u'Moderátor',
    'NOTICE': u'Po aktivaci administrace získáte další práva...',
    'PROMOTED': u'Administrační práva uživateli {} udělena!',
    'DEMOTED': u'Administrační práva uživateli {} odebrána!',

    'TITLE_LOGIN': u'administrátorské přihlášení',
}

statistics = {
    'GENERATED': u'Vygenerováno',
    'UPTIME': u'Uptime',
    'DEBUG': u'Debug',
    'OS': u'Operační systém',
    'UPLOAD_FOLDER': u'Cesta k obrázkům',
    'THUMB_UPLOAD_FOLDER': u'Cesta k náhledům',
    'THUMBNAIL_SIZE': u'Hraniční velikost náhledů',
    'NUM_CATEGORIES': u'Počet kategorií',
    'NUM_USERS': u'Počet uživatelů',
    'NUM_USERS_ADMIN': u'... z toho administrátorů',
    'NUM_USERS_MOD': u'... z toho moderátorů',
    'NUM_REQUESTS': u'Počet požadavků',
    'NUM_REQUESTS_ACCEPTED': u'... z toho schválených',
    'NUM_REQUESTS_DECLINED': u'... z toho neschválenýchh',
    'NUM_REQUESTS_NOACTION': u'... z toho nerozhodnuto',
    'NUM_IMAGES': u'Počet obrázků',
    'NUM_RATING_IMAGES': u'Počet hodnocení obrázků',
    'IMAGE_RATING_POSITIVE': u'... obr. postivních',
    'IMAGE_RATING_NEGATIVE': u'... obr. negativních',
    'IMAGE_RATING_NEUTRAL': u'... obr. neutrálních',
    'NUM_COMMENTS': u'Počet komentářů',
    'NUM_COMMENTS_ACTIVE': u'... z toho aktivních',
    'NUM_COMMENTS_DELETED': u'... z toho smazaných',
    'NUM_RATING_COMMENTS': u'Počet hodnocení komentářů',
    'COMMENT_RATING_POSITIVE': u'... kom. positivních',
    'COMMENT_RATING_NEGATIVE': u'... kom. negativních',
    'COMMENT_RATING_NEUTRAL': u'... kom. neutrálních',
    'AVG_CATEGORY_IMAGE': u'Průměrný počet obrázků na kategorií',
    'AVG_COMMENT_IMAGE': u'Průměrný počet komentářů na obrázek',
    'AVG_RATING_IMAGE': u'Průměrný počet hodnocení na obrázek',
    'AVG_RATING_COMMENT': u'Průměrný počet hodnocení na komentář',

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
    'NEW_CATEGORY': u'nová kategorie',
    'NEW_MODERATOR': u'nový moderátor',

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
