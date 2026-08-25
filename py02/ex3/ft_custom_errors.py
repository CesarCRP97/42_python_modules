
class GardenError(Exception):
	def __init__(self, message: str = "Unknown garden error detected!!"):
		self.message: str = message
		super().__init__(self.message)

class PlantError(GardenError):
	def __init__(self, message: str = "The tomato plant is wilting!"):
		super().__init__(message)

class WaterError(GardenError):
	def __init__(self, message = "Not enough water in the tank!"):
		super().__init__(message)

def ft_custom_errors() -> None:
	
