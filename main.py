from flask import Flask,request
import json

app = Flask(__name__)
# GET requests will be blocked
# GET requests will be blocked
@app.route('/')
def hello():
    return 'Hello There'


@app.route('/json-example', methods=['POST'])
def json_example(request):
    request_data = request.json

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']
            
#     data={"message":"hello_world"}
    


#     self.response.headers['Content-Type'] = 'application/json'   
#     obj = {
#       'success': 'some var', 
#       'payload': 'some var',
#     } 
    try:
        return jsonify(request_data)
    except:
        return 'hi gais'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.0', port=8080, debug=True)
