from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello World"
@app.route("/name")
def myname():
    return "Jatlaa Nikhil"

@app.route('/emp/<int:emp1>')
def show_emp(emp1):
    return 'EMP ID Number: %d' %emp1

@app.route('/num/<float:num1>')
def show_num(num1):
    return 'Number: %f' %num1

if __name__=="__main__":
    app.run()