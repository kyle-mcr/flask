from flask import Flask, render_template  
app = Flask(__name__)    
@app.route('/')        
def hi():
    return "WELCOME!"

@app.route('/play')        
def box():
    return render_template('boxes.html')

@app.route('/play/<times>/<color>/') 
def boxes_qty(times, color):
    return render_template('boxexs_qty.html', num_times=int(times), color=color) 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)