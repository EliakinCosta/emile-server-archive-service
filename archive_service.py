from flask import Flask, jsonify, request, send_file
import settings
import os


app = Flask("archive-service")


@app.route('/save_profile_image', methods=['POST'])
def save_profile_image():
    try:
        file = request.files.get('file')
        old_file_path = request.form.get('old_file_path')
        file_name = file.filename

        if old_file_path:
            os.remove(settings.MEDIA_ROOT + '/' + old_file_path)

        relative_path = "images/user_profile/"
        archive_path = settings.MEDIA_ROOT + '/' + relative_path

        if not os.path.exists(archive_path):
            os.makedirs(archive_path, exist_ok=True)
        file.save(os.path.join(archive_path, file_name))
        return jsonify(result=str('images/user_profile/{0}').format(file_name)), 200
    except Exception as e:
        return jsonify(result=str(e)), 400

@app.route('/files/<path:relative_path>')
def download_file(relative_path):
    directory, filename = str(relative_path).rsplit('/', maxsplit=1)
    format_file = str(filename).split('.')[1]
    archive_url = settings.MEDIA_ROOT + '/' + directory
    return send_file(archive_url + '/' + filename, mimetype='image/{0}}'.format(format_file))


if __name__=='__main__':
    app.run(port=2000)
