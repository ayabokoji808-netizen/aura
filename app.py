from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Grab the X-Forwarded-For header if it exists
    forwarded_for = request.headers.get('X-Forwarded-For')
    
    if forwarded_for:
        # Split the comma-separated string and take the first IP (the real client)
        user_ip = forwarded_for.split(',')[0].strip()
    else:
        user_ip = request.remote_addr

    user_agent = request.headers.get('User-Agent')

    return render_template('index.html', ip=user_ip, user_agent=user_agent)

if __name__ == '__main__':
    app.run(debug=True)
