from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/shutdown", methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server is shutting down....'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)