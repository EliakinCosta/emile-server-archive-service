from flask import Flask, jsonify


app = Flask("archive-service")


@app.route('/save_profile_image/', methods=['GET'])
def save_profile_image():
    return jsonify(result='ok'), 200


if __name__=='__main__':
    app.run()
