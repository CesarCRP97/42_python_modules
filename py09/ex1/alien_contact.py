from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
	RADIO = "radio"
	VISUAL = "visual"
	PHYSICAL = "physical"
	TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
	contact_id: str = Field()
	timestamp: datetime
	location: str = Field(min_length=3, max_length=100)
	contact_type: ContactType
	signal_strength: float = Field(ge=0.0, le=10.0)
	duration_minutes: int = Field(ge=1, le=1440)
	witness_count: int = Field(ge=1, le=100)
	message_received: Optional[str] = Field(None, max_length=500)
	is_verified: bool = False

	@model_validator(mode="after")
	def validate_contact_id(self) -> AlienContact:
		if not self.contact_id.startswith("AC"):
			raise ValueError("Contact ID must start with 'AC'(Alien Contact)")
		if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
			raise ValueError("Physical contact reports must be verified!!!")
		if self.contact_type == ContactType.TELEPATHIC:
			if self.witness_count < 3:
				raise ValueError(
					"Telepathic contacts requires at least 3 witnesses"
				)
		if self.signal_strength > 7.0 and not self.message_received:
			raise ValueError("Strong Signals should include received messages")
		return self


	def print(self) -> None:
		for field, value in self.model_dump().items():
			print(f"{field:<20}: {value}")



def main() -> None:
	print("Alien Contact Log Validation")
	print("\n ==============================================")
	try:
		data = {
			"contact_id": "AC_2024_001",
			"timestamp": datetime.today(),
			"location": "Albacete",
			"contact_type": "radio",
			"signal_strength": 8.5,
			"duration_minutes": 45,
			"witness_count": 5,
			"message_received": "Hola que tal, Albacete caga y vete!!",
			"is_verified": False
		}
		alien_contact_1 = AlienContact(**data)
		alien_contact_1.print()
		print("\n ==============================================")
		print("Trying with invalid data:\n")
		space_station_2 = AlienContact(
			contact_type="telepathic",
			contact_id="AC_2026_042",
			timestamp=datetime(2026, 5, 25),
			location="Bilbao, Euskadi",
			signal_strength=10.0,
			duration_minutes=42,
			witness_count=1,
			message_received="me cago en todos tus muertos",
		)
		space_station_2.print()
	except ValidationError as e:
		for error in e.errors():
			print(error["msg"])

if __name__ == "__main__":
    main()
