from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/pf/pf/<int:x>/<int:y>', methods=['GET'])
def example_pure_function(x, y):
    return str(x + y)


@app.route('/pf/mutable', methods=['GET'])
def mutable():
    mutable_list = [1, 2, 3]
    mutable_list.append(4)
    return f'The result: {mutable_list}'


@app.route('/pf/immutable', methods=['GET'])
def immutable():
    immutable_tupel = (1, 2, 3)
    try:
        result = immutable_tupel.append(4)
    except:
        result = 'You can\'t modify a tupel'
    return f'The result: {result}'


class Book:
    def __init__(self, title):
        self.title = title
        self.lent = False

    def lend(self):
        self.lent = True
        return {"message": f"The book '{self.title}' has been lent."}


@app.route('/pf/oop', methods=['GET'])
def lend_book():
    book = Book("How 2 OOP 101")
    return jsonify(book.lend())


@app.route('/pf/prozedur/<int:n>', methods=['GET'])
def fibonacci(n):
    a, b = 0, 1
    result = ''
    for _ in range(n):
        result += f'{a} '
        a, b = b, a + b
    return result


def say_hello(name):
    return f'Hello, {name}!'


@app.route('/pf/varfun/<name>', methods=['GET'])
def variable_func(name):
    greeting = say_hello
    return greeting(name)


def add(x, y):
    return x + y


def operate(func, x, y):
    return func(x, y)


@app.route('/pf/parfun/<int:x>/<int:y>', methods=['GET'])
def par_as_func(x, y):
    return str(operate(add, x, y))


@app.route('/pf/retfun/<int:x>/<int:y>', methods=['GET'])
def return_func(x, y):
    def multiplier(factor):
        def multiply_by_factor(number):
            return number * factor

        return multiply_by_factor

    multiply_by_two = multiplier(x)
    return str(multiply_by_two(y))


@app.route('/pf/savfun', methods=['GET'])
def save_fun():
    def square(x):
        return x * x

    def cubic(x):
        return x * x * x

    funcs = [square, cubic]
    return str(funcs)


if __name__ == '__main__':
    app.run(debug=True)