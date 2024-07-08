from app.initializers.translator import TRANSLATOR_ENGINE
from common.services.translator.google_translator_repository import GoogleTranslatorRepository
from common.services.translator.translator_repository import TranslatorRepository

class TranslatorFactory():
  @staticmethod
  def create() -> TranslatorRepository:
    if TRANSLATOR_ENGINE == 'google_translator':
      return GoogleTranslatorRepository()
    else:
      raise ValueError(f"Unsupported translator service type: {TRANSLATOR_ENGINE}")