from flask import Flask
app = Flask(__name__)
import random

def random_number():
    return random.randint(0,9)

def make_bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func() + '</b>'
    return wrapper

def make_under(func):
    def wrapper(*args, **kwargs):
        return '<u>' + func() + '</u>'
    return wrapper

def make_ital(func):
    def wrapper(*args, **kwargs):
        return '<i>' + func() + '</i>'
    return wrapper

number = random_number()
print(number)
@app.route('/')
def server():
    return '<h1>Guess a number in the url between 0 and 9!</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'




@app.route('/<int:num>')
def guess(num):
    if num < number:
        return '<h1>To low!!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    if num > number:
        return '<h1>To high!!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if num == number:
        return '<h1>You got it!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)