from bottle import post, request, response
import re
from datetime import datetime
import pdb

questions = {}

@post('/home', method='post')
def my_form():
    email = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME') 
    
    # 7.4. Проверка заполненности полей
    if not all([email, question, username]):
        return "Error: Please fill in all fields"
    
    # 7.1. Проверка формата email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return "Error: Invalid email format"
    
    ###
    questions[email] = question
    pdb.set_trace()
    
    # 7.3. Получаем текущую дату
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 7.2. Формируем ответ с именем пользователя и датой
    return f"""
    Thanks, {username}! 
    The answer will be sent to the mail: {email}
    Access Date: {current_date}
    """

    