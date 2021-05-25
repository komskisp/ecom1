import flask
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = "I\xba7\xa37\xcb\xdcw\x90n\xe7\xbb"



@app.route('/')
def home():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
