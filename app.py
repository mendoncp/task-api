from flask import Flask
from routes import tasks

app = Flask(__name__)

app.register_blueprint(tasks, url_prefix='/tasks/')

if __name__ == "__main__":
    app.run()