from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
import werkzeug

import os

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__, template_folder='template', static_url_path='/static')
api = Api(app)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER






@app.route('/')
@app.route('/index')
def show_index():
    full_filename = 'my-image.png'
    return render_template("index.html", user_image = full_filename)
upload_parser = reqparse.RequestParser(bundle_errors=True)
upload_parser.add_argument(
    'file',
    required=True,
    type=werkzeug.datastructures.FileStorage,
    location='files'
)

# note that location="form" is specified
upload_parser.add_argument(
    "filename",
    required=True,
    type=str,
    location="form"
)


class UploadImage(Resource):
    def post(self):
        args = upload_parser.parse_args()
        image = args.file
        image.save('static/'+args.filename)


api.add_resource(UploadImage, '/uploadimage')

if __name__ == '__main__':
    app.run()

    # you can add back your waitress.serve stuff here
    # but I didn't want to bother in my test environment