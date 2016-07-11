from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
@app.route("/perfect_harmony")
def perfect_harmony():
    return render_template("perfect_harmony.html")

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=1337)