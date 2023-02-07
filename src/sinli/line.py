from enum import Enum
from dataclasses import dataclass


@dataclass
class Line:
    class Field(Enum):
        EXAMPLE = (1, 7, "Example field located in 1st position with length 7")

    # Export to string

    def __str__(self) -> str:
        field_l = []
        # TODO: check that no fields are missing in the definition
        for field in self.Field:
            val = getattr(self, field.name)
            vallen = len(val)
            deflen = field.value[1]

            if vallen < deflen: # pad with spaces
                val = val + "".join([" " for i in range(0, deflen-vallen)])
            elif vallen > deflen: # truncate
                val = val[0:deflen]

            field_l.append(val)

        return "".join(field_l)

    def to_csv(self) -> str:
        return ", ".join(vars(self).values())

    def __repr__(self) -> str:
        return repr(vars(self))

    # TODO: converteix a Line de la mateixa classe però valors diferents
    def to_readable(l: Line) -> dict:
        t = l.tables
        ld = vars(l)
        newld = {}
        for k,v in ld.items():
            # resolve tables
            newld[k] = t.get(k).get(v) or t.get(k).get("??") if t and t.get(k) else v
            # trim str blank spaces and left zeroes
            newld[k] = newld[k].strip().lstrip("0")
        return newld

    # Import

    def from_dict(self, fields: {}):
        for (key, value) in fields.items():
            setattr(self, key, value)
        return self

    @classmethod
    def from_str(cls, line_s: str):
        line_dict = {}
        for field in cls.Field:
            start = field.value[0]
            end = start + field.value[1]
            line_dict[field.name] = line_s[start:end].strip()
            print(f"[DEBUG] {field} → {line_dict[field.name]}")
        line = cls()
        return line.from_dict(line_dict)

@dataclass
class SubjectLine(Line):

    class Field(Enum):
        TYPE = (0, 1, "Tipo de registro (I)")
        FORMAT = (1, 1, "Tipo de formato (N=Normalizado ; ?=Libre)")
        DOCTYPE = (2, 6, "Nombre del tipo de documento")
        VERSION = (8, 2, "Versión del tipo de documento")
        FROM = (10, 8, "Identificador ESFANDE del remitente")
        TO = (18, 8, "Identificador ESFANDE del destinatario")
        LEN = (26, 5, "Cantidad de registros del fichero")
        NUM_TRANS = (31, 7, "Número de transmisión s/emisor")
        LOCAL_FROM = (38, 15, "Usuario local del emisor")
        LOCAL_TO = (53, 15, "Usuario local del destino")
        TEXT = (68, 7, "Texto libre")
        FANDE = (75, 5, "FANDE")

@dataclass
class IdentificationLine(Line):
    class Field(Enum):
        TYPE = (0, 1, "Tipo de registro (I)")
        FROM = (1, 50, "E-mail origen")
        TO = (51, 50, "E-mail destino")
        DOCTYPE = (101, 6, "Tipo de Fichero")
        VERSION = (107, 2, "Versión fichero")
