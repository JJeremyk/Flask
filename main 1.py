from random import randint
from flask import Flask, redirect, url_for
#from db_scripts import get_question_after

quiz = 0 
last_question = 0
def index():
    global quiz, last_question
    max_quiz = 3
    #atau jika siswa menulis get_quiz_count(), maka Anda dapat mengimpornya dan menentukan:
    # max_quiz = max_quiz_count[0]
    quiz = randint(1, max_quiz)
    #atau jika siswa menulis get_quiz_count(), maka Anda dapat mengimpornya dan menentukan:
    # quiz = get_random_quiz_id()
    last_question = 0
    return '<a href = "/test> Test </a>'

def test():
    global last_question
    result = get_question_after(last_question, quiz)
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    else:
        last_question = resuslt[0]
        #Jika kita telah mengajajarkan database untuk mengembalikan Row dan dict, maka kita tidak boleh menulis
        #result[0] dan sebagai gantinya menulis result['id']
        return '<h1>' + str(quiz) + '<br>' + str(result) + '</h1>'

def result():
    return "that's all folks!"
#membuat objek aplikasi web:
app = Flask(__name__)
app.add_url_rule('/', 'index', index) #membuat aturan untuk URL '/'
app.add_url_rule('/test', 'test', test) #membuat aturan untuk URL '/test'
app.add_url_rule('/result', 'result', result) #membuat aturan untuk URL '/result'
if __name__ == "__main__":
    #memulai server web:
    app.run()
