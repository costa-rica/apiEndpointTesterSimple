from flask import Flask, render_template, request, jsonify, make_response, current_app
import os
import json

app = Flask(__name__)
app.secret_key = 'Necessary_to_have'
app.debug = True
app.config['DESTINATION_PASSWORD']='bulljive'


@app.route('/', methods=["GET"])
def get_stuff():
    print('- In post_view endpoint -')

    f = open("headers.json")
    headers_dict = json.load(f)
    f.close()

    f = open("data.json")
    data_dict = json.load(f)
    f.close()

    return render_template("home.html", headers_dict=headers_dict, data_dict=data_dict)


@app.route('/post', methods = ["GET","POST"])
def receive_api_calls():
    print("- In post endpoint -")
    request_headers = request.headers

    print(f"Password received: {request_headers.get('password')}")
    print(f"Password expected: {current_app.config.get('DESTINATION_PASSWORD')}")

    if request_headers.get('password') == current_app.config.get('DESTINATION_PASSWORD'):


        req_head_dict = {i[0]:i[1] for i in request_headers}


        f = open("headers.json", "w")
        json.dump(req_head_dict, f)
        f.close

        request_data = request.get_json()

        f = open("data.json", "w")
        json.dump(request_data, f)
        f.close
        
        return jsonify({"message": "successfully received call!! "})
    else:
        return make_response('Could not verify',401)


if __name__ == '__main__':
    app.run()