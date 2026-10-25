from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
	CADET = "cadet"
	OFFICER = "officer"
	LIEUTENANT = "lieutenant"
	CAPTAIN = "captain"
	COMMANDER = "commander"


class CrewMember(BaseModel):
	member_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=2, max_length=50)
	rank: Rank
	age: int = Field(ge=18, le=80)
	specialization: str = Field(min_length=3, max_length=30)
	years_experience: int = Field(ge=0, le=50)
	is_active: bool = True




class SpaceMission(BaseModel):
	mission_id: str = Field(min_length=5, max_length=15)
	mission_name: str = Field(min_length=3, max_length=100)
	destination: str = Field(min_length=3, max_length=50)
	launch_date: datetime
	duration_days: int = Field(ge=1, le=3650)
	crew: list[CrewMember] = Field(min_length=1, max_length=12)
	mission_status: str = "planned"
	budget_millions: float = Field(ge=1.0, le=10000.0)

	@model_validator(mode="after")
	def validate_mission(self) -> SpaceMission:
		if not self.mission_id.startswith("M"):
			raise ValueError("Mission ID must start with 'M'")
		if not self.at_least_one_captain_or_better_in_crew(self.crew):
			raise ValueError("Crew must have at least one Commander or Captain")
		if self.duration_days > 365:
			msg = "Long missions (> 365 days) need 50\%" \
			" experienced crew (5+ years)"
			if self.get_percentage_experienced(self.crew) < 50.0:
				raise ValueError(msg)
		if not all_members_are_active(self.crew):
			raise ValueError("All crew members must be active")

	def at_least_one_captain_or_better_in_crew(crew: list[CrewMember]) -> bool:
		for member in crew:
			if member.rank in [Rank.CAPTAIN, Rank.COMMANDER]:
				return True
		return False

	def get_percentage_experienced(crew: list[CrewMember]) -> float:
		pass

	def all_members_are_active(crew: list[CrewMember]) -> bool:
		pass


def main() -> None:


if __name__ == "__main__":
    main()

