#!/usr/bin/python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

	def __init__(self):
		super().__init__()
		self._data: list[str] = []
		self._rank : int = 0

	@abstractmethod
	def validate(self, data: Any) -> bool:
		pass

	@abstractmethod
	def ingest(self, data: Any) -> None:
		pass

	def output(self) -> tuple[int, str]:
		if len(self._data) == 0:
			raise Exception("No data available")
		value : str = self._data.pop(0)
		# todo: quitar print test:
		print(f"{self._data}")
		rank : int = self._rank
		self._rank += 1
		return rank, value

class NumericProcessor(DataProcessor):
	def validate(self, data: Any) -> bool:
		if isinstance(data, int) or isinstance(data, float):
			return True
		if isinstance(data, list):
			for item in data:
				if not(isinstance(item, int) or isinstance(item, float)):
					return False
			return True
		return False

	def ingest(self, data: int | float | list[int | float]) -> None:
		if not self.validate(data):
			raise Exception("Improper numeric data")
		if isinstance(data, int) or isinstance(data, float):
			self._data = self._data.append(str(data))
		else:
			for item in data:
				self._data = self._data.append(str(item))




class TextProcessor(DataProcessor):

	def validate(self, data: Any) -> bool:
		if isinstance(data, dict):
			return True
		if isinstance(data, list):
			for item in data:
				if not isinstance(item, str):
					return False
			return True
		return False

	def ingest(self, data: str | list[str]) -> None:
		if not self.validate(data):
			raise Exception("Improper text data")
		if isinstance(data, str):
			self._data = self._data.append(str(data))
		else:
			for item in data:
				self._data = self._data.append(str(item))


class LogProcessor(DataProcessor):
	def validate(self, data: Any) -> bool:
		if isinstance(data, dict):
			for key in data:
				if not isinstance(key, str):
					return False
				if not isinstance(data[key], str):
					return False
			return True
		if isinstance(data, list):
			for item in data:
				if not isinstance(item, dict):
					return False
				for key in item:
					if not isinstance(key, str):
						return False
					if not isinstance(item[key], str):
						return False
			return True
		return False

	def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
		if not self.validate(data):
			raise Exception("Improper log data")
		if isinstance(data, dict):
			self._data = self._data.append(str(data))
		else:
			for item in data:
				self._data = self._data.append(str(item))
