from abc import ABC, abstractmethod

class TranslatorRepository(ABC):
  @abstractmethod
  def translate(self, text: str, dest: str) -> str:
    pass