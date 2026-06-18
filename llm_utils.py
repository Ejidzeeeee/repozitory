"""
LLM утилиты: запросы к Ollama, генерация summary, классификация
"""
import requests
import json

def llm_generate(prompt, model="qwen2.5", url="http://localhost:11434/api/generate"):
    """Отправляет запрос к локальной Ollama."""
    try:
        payload = {"model": model, "prompt": prompt, "stream": False}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            return f"Ошибка: {response.status_code}"
    except Exception as e:
        return f"Ошибка подключения: {e}"

def generate_summary(record):
    """Генерирует краткое описание кандидата."""
    prompt = f"Сгенерируй одно предложение на русском языке, которое резюмирует ключевой опыт и профессиональные качества соискателя. Данные: {record}"
    return llm_generate(prompt)

def assess_fit(record):
    """Оценивает соответствие кандидата желаемой должности от 1 до 5."""
    prompt = f"Оцени соответствие кандидата желаемой должности по шкале от 1 до 5. Данные: {record}. Ответь только числом."
    response = llm_generate(prompt)
    try:
        return int(response.strip())
    except:
        return 3

def generate_title(text):
    """Генерирует заголовок для текста."""
    prompt = f"Сгенерируй краткий заголовок (не более 10 слов) для этого текста:\n{text}"
    return llm_generate(prompt)

def classify_area(record):
    """Классифицирует профессиональную область кандидата."""
    prompt = f"Определи профессиональную область кандидата из списка: IT, Телекоммуникации, Медицина, Строительство, Финансы, Маркетинг, Продажи, Логистика, Производство, Образование, Другое. Данные: {record}. Ответь только названием категории."
    return llm_generate(prompt)

def classify_grade(record):
    """Определяет грейд кандидата (Junior/Middle/Senior/Lead/Top)."""
    prompt = f"Определи уровень квалификации кандидата (Junior/Middle/Senior/Lead/Top). Данные: {record}. Ответь только названием уровня."
    return llm_generate(prompt)
