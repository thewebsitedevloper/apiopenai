from flask import Flask, render_template, request
from chatgptbot import chatgptbot.py

app = Flask(__name__)
chatbot = chatgptbot.py()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"]
    response = chatbot.get_response(message)

    # Add the message and response to the chat history
    # ...

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
