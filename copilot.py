# Во-первых, установите и импортируйте openai и python-dotenv:
import os
import json
from dotenv import load_dotenv
import openai

# Создайте класс с именем Copilot и добавьте две функции:
# clear_text — отвечает за очистку лишних пробелов.
# get_answer — отвечает за получение ответа. Вызывает класс Completion из библиотеки openai. Для того, чтобы продолжить наш запрос, нам нужен API-ключ.

class Copilot:

	def clear_text(self, text):
		a = text.replace("\n", " ")
		b = a.split()
		c = " ".join(b)

		return c

	def get_answer(self, question):
		prompt = question

		load_dotenv()

		openai.api_key = os.getenv("CHAT_GPT3_API_KEY")
		response = openai.Completion.create(
			engine="text-davinci-003",
			prompt=prompt,
			max_tokens=512,
			temperature=0.5,
		)

		json_object = response

		# Convert the JSON object to a JSON string
		json_string = json.dumps(json_object)

		# Parse the JSON string using json.loads()
		parsed_json = json.loads(json_string)

		text = parsed_json['choices'][0]['text']
		cleared_text = self.clear_text(text)

		return cleared_text
