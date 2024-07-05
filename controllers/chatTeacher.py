from app import app


@app.route('/chatTeacher')
def chat():

    return 'teacher/chat.html'
