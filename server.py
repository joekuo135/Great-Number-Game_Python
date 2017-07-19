from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key ='mykey'


@app.route('/')
def index():
    if 'message' not in session:
        session['message'] = ''
    if 'number' not in session:
        session['number'] = random.randrange(0, 101)
    return render_template('index.html', message = session['message'], number= session['number'])

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['number'])

    if guess == session['number']:
        session['message'] = 'You Win! '+str(session['number'])+' was the number!'
    if guess > session['number']:
        session['message'] = 'Number is Too High! Guess Lower!'
    elif guess < session['number']:
        session['message'] = "Number is Too Low! Guess Higher!"

        # print guess
    return redirect('/')

@app.route('/reset')
def reset():
  
    session.pop('number')
    session.pop('message')
    return redirect('/')

app.run(debug=True)