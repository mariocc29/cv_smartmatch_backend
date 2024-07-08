from googletrans import Translator

from common.services.translator.translator_repository import TranslatorRepository

class GoogleTranslatorRepository(TranslatorRepository):
  def translate(self, text: str, dest: str) -> str:
    translator = Translator()
    src = translator.detect(text).lang
    if src != dest:
      return translator.translate(text, dest=dest, src=src).text
    return text