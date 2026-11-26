from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    varName = request.form.get("parName")
    if not varName:
        varName = "Anonim"
    return f"<h2>Halo, {varName}! wellcome di web gw kuhkuhkuh</h2>"

if __name__ == "__main__":
    app.run(debug=True)