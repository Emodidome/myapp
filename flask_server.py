from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('donut.html')

# @app.route('/welcome', methods=['POST'])
# def welcome():
#     data = request.get_json()
#     name = data.get('name', '').strip()
    
#     if name:
#         return jsonify({'message': f'Hello, {name}.'})
#     else:
#         return jsonify({'error': 'Please enter a name'}), 400

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)