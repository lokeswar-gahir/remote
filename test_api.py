from flask import Flask, request, jsonify
app = Flask(__name__)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b


@app.route('/add', methods= ['GET','POST'])  
def fu():
    if (request.method == 'POST'):
        try:
            ops = request.json["operation"]
            a = request.json["a"]
            b = request.json["b"]
            d = {1:add, 2:sub, 3: mul, 4:divide}
            result = d[ops](a,b)
            output = f"the answer is {result}."
            return jsonify(output)
        except Exception as e:
            output = f"some ERROR has occurred : {str(e)} "
            return jsonify(output)

if __name__ == '__main__':
    app.run()