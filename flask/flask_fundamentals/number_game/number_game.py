from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])         
def result():
    print("Got Post Info")
    print(request.form)
    import random
    if 'answer' not in session.keys():
        session['answer']= random.randint(1,100)
    print(session['answer'])
    number_from_form = request.form['number']
    session['number'] = int(request.form['number'])
    if session['answer'] == session['number']:
        return redirect('/win')
    else:
        if session['number'] > session['answer']:
            return redirect('/high')
        else:
            return render_template("form.html", number=request.form['number'])
@app.route('/high')
def lose():
    return render_template("high.html", number=session['number']) 

@app.route('/win')
def win():
    return render_template("win.html") 

if __name__=="__main__":   
    app.run(debug=True)