from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/pdfs', methods=['POST', 'GET']) 
def foo():
    # data = request.json
    
    return send_file('/Users/ruby/Documents/2022/VideoGame/code/layout-and-printing/1686082716.pdf', as_attachment=True)

