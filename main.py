import uuid
from flask import Flask, send_from_directory, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def peach_pass_main():
    return send_from_directory('static', 'main.html')

@app.route("/payment")
def payment_details():
    return send_from_directory('static', 'payment_details.html')

@app.route('/main.css')
def peach_style():
    return send_from_directory('static', 'main.css')

@app.route('/hacked')
def payment():
    return send_from_directory('static', 'hacked.html')

# @app.route("/submit_payment", methods=['POST', 'GET'])
# def submit_payment_callback():
#     print(request.method)
#     print('request')
#     print(request.form.__dict__)
#     with open('payments/' + str(uuid.uuid4()) + '.txt', 'w') as f:
#         f.write('hello molly')
#     return redirect(url_for('peach_pass_main'))

@app.route("/images/<image_name>")
def load_image(image_name):
    return send_from_directory('static', image_name)

if __name__ == '__main__':
    app.run()
