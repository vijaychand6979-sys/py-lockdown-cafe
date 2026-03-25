from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError
        if (
            visitor.get("vaccine").get("expiration_date")
            < datetime.date.today()
        ):
            raise OutdatedVaccineError
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
