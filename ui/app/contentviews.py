from app import *

@app.route("/", methods=["GET"])
def test():
   return render_template("<h1>I am a heading</h1>")