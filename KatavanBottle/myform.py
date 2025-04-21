from bottle import post, request, response
import re
import json
from datetime import datetime
import os

JSON_FILE = 'questions.json'

def load_data():
    
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_data(data):

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@post('/home', method='post')
def my_form():
    email = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    
    if not all([email, question, username]):
        return "Ошибка: Пожалуйста, заполните все поля"
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return "Ошибка: Неправильный формат email"
    
    if len(question.strip()) <= 3:
        return "Ошибка: Вопрос должен содержать более 3 символов"
    if question.strip().isdigit():
        return "Ошибка: Вопрос не может состоять только из цифр"
    
    data = load_data()
    
    if email in data:
        if question not in data[email]['questions']:
            data[email]['questions'].append(question)
        else:
            return "Ошибка: Такой вопрос уже был задан ранее"
    else:
        data[email] = {
            'username': username,
            'questions': [question],
            'first_access': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    save_data(data)
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"""
    Спасибо, {username}! 
    Ответ будет отправлен на почту: {email}
    Дата обращения: {current_date}
    """