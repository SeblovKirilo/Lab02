# Імпорт бібліотек
from datetime import date

def today_is():
    # Повертаємо поточну дату. У форматі ДД-ММ-РР
    return f"<p>Today is {date.today().strftime('%d-%m-%Y')}</p>"
