from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Capture client connection details
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Unknown')
    
    # Pass both variables into index.html
    return render_template("index.html", ip=client_ip, browser=user_agent)

if __name__ == "__main__":
    app.run(debug=True)