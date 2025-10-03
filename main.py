from flask import Flask
import requests  # Dependency để test

app = Flask(__name__)

@app.route('/')
def hello():
    response = requests.get('https://httpbin.org/ip')  # Gọi API để dùng requests
    return f"Hello, World! Your IP: {response.json().get('origin', 'Unknown')}"

if __name__ == '__main__':
    app.run(debug=True)