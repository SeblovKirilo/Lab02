# Імпорт бібліотек
from flask import Flask, request
from datetime import date

# Назва застосунку
app = Flask(__name__)

@app.route("/")
def today_is():
    # Повертаємо поточну дату. У форматі ДД-ММ-РР
    return f"<p>Today is {date.today().strftime('%d-%m-%Y')}</p>"
