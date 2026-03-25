class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return ("Not Vaccinated!")


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return ("Expired Vaccination!")


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return ("Not wearing a mask!")
