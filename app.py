from flask import Flask
from calculate import main

app = Flask(__name__)

@app.route('/')
def home():
    main()
    return "Hello, Railway! Your Flask app is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)