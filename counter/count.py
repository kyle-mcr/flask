from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def count():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 0
    return render_template("index.html", count = session['count'])

@app.route('/reset')         
def reset():
    session.pop('count')
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)   