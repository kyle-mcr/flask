from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello():
    #return 'Hello World!!!!!'  # Return the string 'Hello World!' as a response
    return render_template('index.html')

@app.route('/success')
def success():
    return "success"

@app.route('/<name>/<times>' ) 
def hello_person(name, times):
    print("in the hello person function")
    print("*"*80)
    return render_template('name.html', some_name=name, num_times=int(times)) 

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)