# ollamaL.py - очищенная версия

from litellm import completion

MODEL = "ollama_chat/gemma4:e4b"
API_BASE = "http://127.0.0.1:11434"

class User_chat_Ollama:
    def __init__(self):
        self.messages = []
        self.MODEL = MODEL
        self.API_BASE = API_BASE

    def add_question(self, question: str) -> str:
        self.messages.append({"role": "user", "content": question})
        response = completion(
            model=self.MODEL,
            messages=self.messages,
            api_base=self.API_BASE,
            request_timeout=360,
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})
        return answer

    def __str__(self):
        answer = ""
        for dicts in self.messages:
            if dicts["role"] == "assistant":
                answer += "Ответ от LLM: " + dicts['content'] + "\n"
            elif dicts["role"] == "user":
                answer += "Ваш вопрос: " + dicts['content'] + "\n"
        return answer

    def clear_chat_user(self, *args, **kwargs):
        if "number" in kwargs:
            self.messages.pop(kwargs['number'])
            self.messages.pop(kwargs['number'])
            return "Сообщение было удалено!"
        if "question" in kwargs:
            for dicts in self.messages:
                if dicts['content'] == kwargs['question']:
                    ind = self.messages.index(dicts)
                    self.messages.pop(ind)
                    self.messages.pop(ind)
                    return "Сообщение было удалено!"
        self.messages = []
        return "Весь чат был удален!"