from flask import Flask, jsonify, request
import settings
import os


app = Flask("archive-service")


@app.route('/save_profile_image', methods=['POST'])
def save_profile_image():
    try:
        print(request.files)
        file = request.files['image_file']
        file_name = file.filename

        caminho_relativo = "images/user_profile/"
        url_arquivo = settings.MEDIA_ROOT + '/' + caminho_relativo
        if not os.path.exists(url_arquivo):
            os.makedirs(url_arquivo, exist_ok=True)
        file.save(os.path.join(url_arquivo, file_name))
        jsonify(result='ok'), 200
    except Exception as e:
        return jsonify(result=str(e)), 400


if __name__=='__main__':
    app.run(port=2000)
