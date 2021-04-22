from flask import Flask

app = Flask(__name__)

a=2
b=3

@app.route("/")
def index():
    return "The sum is : " + str(a+b)

@app.route("/sub")
def sub():
    return "The difference is : " +str(a-b)

@app.route("/mul")
def mul():
    return "The product is : " +str(a*b)

@app.route("/power")
def power():
    return "The power is : " +str(a**b)

@app.route("/exp")
def exp():
    return "The expression is : " +str(a*b+a**b)

#"Hello, world!"


if __name__ == "__main__":
    app.run()

#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Hello, world!"


#if __name__ == "__main__":
#    app.run()

