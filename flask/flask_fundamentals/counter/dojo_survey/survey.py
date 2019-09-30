from flask import Flask, render_template, request, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    return render_template("form.html", name=request.form['name'], location=request.form['location'], language=request.form['language'])

if __name__ == "__main__":
    app.run(debug=True)