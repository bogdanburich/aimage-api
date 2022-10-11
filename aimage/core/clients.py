import openai

from .config import MAX_TOKENS, MODEL, TEMPERATURE


class OpenAIClient(openai.Completion):

    def get_response(self, text) -> dict:
        response = self.create(
            model=MODEL,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            prompt=text,
        )
        return response.data

    def get_text(self, *args) -> str:
        response = self.get_response(*args)
        text = response['choices'][0]['text']
        return text.strip().replace('\n', ' ')
