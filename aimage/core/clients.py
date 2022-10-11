from typing import Optional

import openai
from django.conf import settings
from pydalle import Dalle

from .config import MAX_TOKENS, MODEL, TEMPERATURE


class OpenAIClient(openai.Completion):

    def get_response(self, text) -> dict:
        response = self.create(
            model=MODEL,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            prompt=text,
        )
        return response

    def get_text(self, *args) -> str:
        response = self.get_response(*args)
        text = response['choices'][0]['text']
        return text.strip().replace('\n', ' ')


class DalleClient(Dalle):

    def __init__(self, headers: Optional[dict] = None):
        username = settings.DALLE_USERNAME
        password = settings.DALLE_PASSWORD
        super().__init__(username, password, headers)
