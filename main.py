import flask
from flask import request
from flask import render_template
from flask import send_from_directory
from flask import Flask
app = Flask(__name__)
data= []
@app.route('/')
def get():
    return render_template('solver.html',data="6LfN97MUAAAAACDHtVJB2FjKaqj0mnPYZejkPW7o")

@app.route('/bank',methods=['POST','GET'])
def bank():
    global data
    if request.method == 'POST':
        data.append(request.form['g-recaptcha-response'])
        return render_template('solver.html',data="6LfN97MUAAAAACDHtVJB2FjKaqj0mnPYZejkPW7o")
    else:
        return str(data)
if __name__ == '__main__':
    app.run("127.0.0.1",port=5000,debug=True)
