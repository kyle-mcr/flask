from flask import Flask, render_template  
app = Flask(__name__)    
@app.route('/')        
def hi():
    return "WELCOME!"

@app.route('/play')        
def box():
    return render_template('checkers.html')

@app.route('/play/<times>/') 
def boxes_qty(times):
    return render_template('checkers.html', num_times=int(times))

if __name__=="__main__":
    app.run(debug=True)