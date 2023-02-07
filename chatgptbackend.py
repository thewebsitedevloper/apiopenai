from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template<"("html.index")
@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"]

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
