from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.debug = True

def get_client_ip(request):
    """Lấy địa chỉ IP thực của client, kể cả khi qua proxy."""
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.remote_addr
    return ip

@app.route('/')
def login():
    ip_address = get_client_ip(request)
    print(f"IP Address: {ip_address}")  # In ra console để kiểm tra
    return render_template('index.html', ip_address=ip_address)

@app.route('/home')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1314, debug=True)