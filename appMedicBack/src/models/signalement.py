from datetime import datetime


class Signalement:
    def __init__(self, pseudo: str, code_cip: str):
        self.pseudo = pseudo
        self.code_cip = code_cip
        self._validate_cip()
        self.date_created = datetime.now()

    def _validate_cip(self):
        if (
            not (len(self.code_cip) == 7 or len(self.code_cip) == 13)
            or not self.code_cip.isdigit()
        ):
            error = "Le code CIP doit être un nombre à 7 ou 13 chiffres."
            raise ValueError(error)

    def to_dict(self):
        return {
            "pseudo": self.pseudo,
            "code_cip": self.code_cip,
            "date_created": self.date_created,
        }
