from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
translator = Translator()

@app.route('/', methods=['GET'])
@app.route('/chat/completions', methods=['POST'])
def index():
    if request.method == 'GET' : return 'Please Use POST Method Instead GET Method.'
    req_content = request.get_json()
    print('[LOG] REQUEST_CONTENT_JSON :', req_content)
  
    req_content = req_content['messages'][-1]['content']
    print(f'[LOG] REQUEST_CONTENT_PROMPT : {req_content}')

    dest_and_src = request.get_json().get('model').split('-')
    dest = dest_and_src[1]
    src = dest_and_src[0]

    ret_content = translator.translate(req_content, src=src, dest=dest)
    ret_content = ret_content.text
    print(f'[LOG] RETURN_CONTENT : {ret_content}')

    return jsonify({'choices' : [{'message' : {'content' : ret_content}}]})

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=__import__('random').randint(80, 9999))
