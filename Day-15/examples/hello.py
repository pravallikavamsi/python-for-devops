from flask import Flask

#creating flask app instance
app = Flask(__name__)

#adding decorators
@app.route("/")
def hello():
    return 'hello world'

app.run('0.0.0.0')
