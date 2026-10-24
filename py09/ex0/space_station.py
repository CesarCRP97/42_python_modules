#!/usr/bin/python3

from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
	station_id : str = Field(min_length=3, max_length=10)
	name : str = Field(min_length=1, max_length=50)
	crew_size : int = Field(ge=1, le=20)
	power_level : float = Field(ge=0.0, le=100.0)
	oxygen_level : float = Field(ge=0.0, le=100.0)
	last_maintenance : datetime
	is_operational : bool = True
	notes : Optional[str] = Field(None, max_length=200)

	def print(self) -> None:
		for field, value in self.model_dump().items():
			print(f"{field:<20}: {value}")



def main() -> None:
	print("Space Station Data Validation")
	print("\n ==============================================")
	data = {
		"station_id": "123abc",
		"name": "ISS_americano",
		"crew_size": 2,
		"power_level": 81.3,
		"oxygen_level": 42.0,
		"last_maintenance": datetime.today(),
		"notes": "Hay armitas a bordo"
	}
	space_station_1 = SpaceStation(**data)
	space_station_1.print()
	print("\n ==============================================")
	try:
		print("Trying with invalid data:\n")
		space_station_2 = SpaceStation(
			station_id="holawi",
			name="alsjdjlkasd",
			crew_size=21,
			power_level=100.0,
			oxygen_level=30.0,
			last_maintenance=datetime.today(),
			notes=""
		)
		space_station_2.print()
	except ValidationError as e:
		for error in e.errors():
			print(f"Validation Error: {error["msg"]}")

if __name__ == "__main__":
    main()
