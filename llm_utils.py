"""
Утилиты для работы с LLM 
"""
import requests

class LLMClient:
    """Клиент для отправки запросов к локальной LLM."""
    def __init__(self, url="http://localhost:11434/api/generate", model="qwen2.5"):
        self.url = url
        self.model = model
    
    def generate(self, prompt, stream=False):
        """Отправляет запрос к LLM и возвращает ответ."""
        try:
            payload = {"model": self.model, "prompt": prompt, "stream": stream}
            response = requests.post(self.url, json=payload)
            if response.status_code == 200:
                return response.json().get("response", "")
            return f"Ошибка {response.status_code}"
        except Exception as e:
            return f"Ошибка подключения: {e}"
    
    def ask(self, prompt, system_prompt=None):
        """Универсальный метод для любого запроса."""
        full_prompt = f"{system_prompt}\n{prompt}" if system_prompt else prompt
        return self.generate(full_prompt)

def create_prompt(template, **kwargs):
    """Заполняет шаблон промпта значениями."""
    return template.format(**kwargs)
