from flask import Flask  
app = Flask(__name__)   
@app.route('/')
def hello_world():
    return "Hello Lyle and World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def name(name):
    print("*"*80)
    return f"Hello {name}!"

@app.route('/repeat/<word>/<number>')
def repeat(word, number):
    return f"{word} "* int(number)


if __name__=="__main__":
    app.run(debug=True)