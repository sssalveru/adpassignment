from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        keys_list = list(some_json)
        ans = some_json[keys_list[0]] + some_json[keys_list[1]]
        return jsonify({'answer': ans})
    else:
        return jsonify({"error":"Enter two numbers"})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)


# @app.route('/')
# def my_form():
#     return render_template('my-form.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     text1 = request.form['text1']
#     answer = int(text) + int(text1)
#     return render_template('my-form.html',ans=str(answer))  

# if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=8000,debug=True)

