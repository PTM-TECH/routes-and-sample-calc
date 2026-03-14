from flask import Flask

app = Flask(__name__)

@app.route('/print/<message>')
def print_message(message):
    return f"<h1>{message}</h1>"

@app.route('/count/<int:num>')
def count(num):
    return "<br>".join(str(n) for n in range(num + 1))

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Unsupported operation", 400
    return f"<h1>{num1} {operation} {num2} = {result}</h1>"