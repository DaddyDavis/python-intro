from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cassie_homepage():
    return render_template('cassie_love.html')

@app.route("/api/v1/status")
def status_check():
    return {"status": "online", "code_name": "Odin", "ram_used": "low"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
