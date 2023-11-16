from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

def run_cpp_program(user_input):
    try:
        result = subprocess.check_output(["Search_Engine.exe", user_input], text=True)
        return result
    except subprocess.CalledProcessError as e:
        return "Error running C++ program: " + str(e)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = run_cpp_program(user_input)
        return jsonify({"result": result})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
