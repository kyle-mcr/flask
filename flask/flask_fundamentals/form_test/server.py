from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("form.html")
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')
    
@app.route('/show')
def show_user():
    return render_template("info.html", name=request.form['name'], em=request.form['email'])

if __name__ == "__main__":
    app.run(debug=True)
