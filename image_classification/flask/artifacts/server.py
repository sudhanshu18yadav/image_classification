from flask import Flask, request, jsonify
import psutil


app = Flask(__name__)

@app.route('/classify_image',method = ['GET','POST'])
def classify_image():
    return 'hi'


if __name__ == "__main__":
    app.run(port=5000)
