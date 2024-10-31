from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/insert/<text>", methods=["POST"])
def insert_text(text):
    with open("response.txt", "w") as file:
        file.write(text)
    return f"message Text saved successfully: {text}"

@app.route("/api/get", methods=["GET"])
def get_text():
    try:
        with open("response.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        text = ""
    return text

if __name__ == "__main__":
    app.run(debug=True)
