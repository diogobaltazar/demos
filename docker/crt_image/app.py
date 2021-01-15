import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return 'Hello, %s' %os.environ.get('USER_NAME')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '8080')