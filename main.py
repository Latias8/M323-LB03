from flask import Flask, jsonify
from functools import reduce

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


@app.route('/pf/closure', methods=['GET'])
def closure():
    def outer_function(x):
        def inner_function(y):
            return x + y

        return inner_function

    add_five = outer_function(5)
    return str(add_five(3))


@app.route('/pf/lambda', methods=['GET'])
def lambda_():
    greet = lambda: "Hello, World!"
    return str(greet())


@app.route('/pf/lambdawa', methods=['GET'])
def lambdawa_():
    square = lambda x: x**2
    return str(square(2))


@app.route('/pf/map', methods=['GET'])
def map_func():
    def square(x):
        return x ** 2

    squares = map(square, [1, 2, 3, 4])
    return list(squares)


@app.route('/pf/filter', methods=['GET'])
def filter_func():
    def is_even(x):
        return x % 2 == 0

    even_numbers = filter(is_even, [1, 2, 3, 4, 5])
    return list(even_numbers)


@app.route('/pf/reduce', methods=['GET'])
def reduce_func():
    def multiply(x, y):
        return x * y

    numbers = [1, 2, 3, 4]
    product_of_numbers = reduce(multiply, numbers)
    return str(product_of_numbers)


@app.route('/pf/mapfilred', methods=['GET'])
def mapfilred():
    products = [
        {"name": "Laptop", "price": 1200},
        {"name": "Smartphone", "price": 700},
        {"name": "Tablet", "price": 300},
        {"name": "Monitor", "price": 450},
        {"name": "Keyboard", "price": 50}
    ]

    expensive_products = filter(lambda product: product["price"] > 400, products)
    discounted_products = map(lambda product: {"name": product["name"], "price": product["price"] * 0.8}, expensive_products)
    total_price = reduce(lambda acc, product: acc + product["price"], discounted_products, 0)
    return str(total_price)


@app.route('/pf/aggregation', methods=['GET'])
def aggregation():
    orders = [
        {"product": "Laptop", "quantity": 2, "unit_price": 1200, "manufacturer": "Us"},
        {"product": "Smartphone", "quantity": 5, "unit_price": 700, "manufacturer": "Partner A"},
        {"product": "Tablet", "quantity": 7, "unit_price": 300, "manufacturer": "Us"},
        {"product": "Monitor", "quantity": 3, "unit_price": 450, "manufacturer": "Partner B"},
        {"product": "Keyboard", "quantity": 10, "unit_price": 50, "manufacturer": "Us"}
    ]

    sales_per_product = map(lambda order: {"product": order["product"], "total_sales": order["quantity"] * order["unit_price"], "manufacturer": order["manufacturer"]}, orders)
    our_products_sales = filter(lambda order: order["manufacturer"] == "Us", sales_per_product)
    total_sales = reduce(lambda acc, order: acc + order["total_sales"], our_products_sales, 0)
    return str(total_sales)


@app.route('/pf/factorial/<int:n>', methods=['GET'])
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return str(result)


@app.route('/pf/algwithfunc', methods=['GET'])
def algwithfunc():
    def square(x):
        return x ** 2

    def addition(a, b):
        return a + b

    def sumofem(x, y):
        sq_x = square(x)
        sq_y = square(y)
        return addition(sq_x, sq_y)

    result = sumofem(420, 69)
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)