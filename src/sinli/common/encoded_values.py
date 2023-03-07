from pycountry import countries, languages
from enum import Enum, auto

class BasicType(Enum):
    DATE6=auto(), # MMAAAA
    DATE8=auto(), # AAAAMMDD
    STR=auto(),
    INT=auto(),
    BOOL=auto(),
    LANG=auto(),
    COUNTRY=auto(),
    CURRENCY1=auto(), # "P"|"E"
    CURRENCY3=auto(), # ISO-4217. ex: EUR
    #LIST_SEMICOLON
    #LIST_SLASH

class SinliCode(Enum):
    BINDING =  {
        "??": "Sin especificar",
        "01": "Tela",
        "02": "Cartoné",
        "03": "Rústica",
        "04": "Bolsillo",
        "05": "Troquelado",
        "06": "Espiral",
        "07": "Anillas",
        "08": "Grapado",
        "09": "Fascículo encuadernable",
        "10": "Otros",
    },
    TB_REGION = {
        "??": "Sin especificar",
        "00": "Sin asignación a Comunidad Autónoma concreta",
        "01": "ANDALUCÍA",
        "02": "ARAGÓN",
        "03": "PRINCIPADO DE ASTURIAS",
        "04": "ISLAS BALEARES",
        "05": "CANARIAS",
        "06": "CANTABRIA",
        "07": "CASTILLA-LA MANCHA",
        "08": "CASTILLA y LEÓN",
        "09": "CATALUÑA",
        "10": "EXTREMADURA",
        "11": "GALICIA",
        "12": "MADRID",
        "13": "REGIÓN DE MURCIA",
        "14": "NAVARRA",
        "15": "PAÍS VASCO",
        "16": "LA RIOJA",
        "17": "COMUNIDAD VALENCIANA",
        "18": "CIUDAD DE CEUTA",
        "19": "CIUDAD DE MELILLA",
        "99": "Asignado a todas las Comunidades Autónomas",
    },
    STATUS = {
        "0": "Disponible",
        "1": "Sin existencias pero disponible a corto plazo",
        "2": "Sin existencias indefinidamente",
        "3": "En reimpresión",
        "4": "Novedad. Próxima publicación",
        "5": "Sustituye edición antigua",
        "6": "Impresión bajo demanda 1x1",
        "7": "No pertenece a nuestro fondo o no identificado",
        "8": "Agotado",
        "9": "Descatalogado",
    },
    READ_LEVEL = {
        "0": "Sin calificar",
        "1": "De 0 a 4 años",
        "2": "De 5 a 6 años",
        "3": "De 7 a 8 años",
        "4": "De 9 a 10 años",
        "5": "De 11 a 12 años",
    },
    AUDIENCE = {
        "000": "Sin calificar",
        "100": "Infantil hasta 12 años",
        "200": "Juvenil de 13 a 15 años",
        "300": "Textos",
        "400": "General",
    },
    TYPE = {
        "00": "sin calificar",
        "10": "libro",
        "20": "audio",
        "30": "video",
        "40": "cd-rom",
        "50": "dvd",
        "60": "otros",
    }
