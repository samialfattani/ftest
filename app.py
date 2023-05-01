from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# if __name__ == "__main__":

if __name__ == '__main__':
    p = os.environ.get('PORT')
    p = p if p else '5051'
    print(f"https://localhost:{p}")
    print(f"https://127.0.0.1:{p}")
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=p) # Waitress
    app.run() # default
