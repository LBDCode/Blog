from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_methhod():
    return "Hello world!"


if __name__ == '__main__':
    app.run()

