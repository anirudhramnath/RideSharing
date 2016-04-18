from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<strong>{a: 5, b:10}</strong>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')