import re


class Validator:

    def __init__(self):
        """
        Create Validator instance
        """
        return

    def validate_nif_nie(self, nif_nie: str):
        """
        Returns if a provided DNI is valid or not.

        Arguments:
            nif_nie (str): the spanish id number to validate.
        """
        # TODO: Validate also passports and others (for foreigners)
        # Check the format
        nif_nie = re.sub("[-, ]", "", nif_nie).strip()
        if not re.match("^[0-9]{8,8}[A-Za-z]$", nif_nie):
            return False
        # Check the letter
        _letter = 'TRWAGMYFPDXBNJZSQVHLCKE'[int(nif_nie[:-1]) % 23]
        if nif_nie[-1] != _letter:
            return False
        return True

    def validate_email(self, email: str):
        """
        Returns if the provided email is a valid UPM email account.

        Arguments:
            email (str): the email to validate.
        """
        if not re.match(".*@(?:alumnos.upm.es|upm.es|.*.upm.es)$", email):
            return False
        return True

    def validate_type(self, type: str):
        if not re.match("(:?access|exit)$", type):
            return False
        return True

    def validate_event(self, event):
        if (self.validate_email(event.email)
            and self.validate_type(event.type)
                and self.validate_nif_nie(event.nif_nie)):
            return True
        return False