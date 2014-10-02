#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mimetypes
import os
import rrr

from flask import Flask, make_response, request, render_template
from flask.ext.heroku import Heroku
from werkzeug import secure_filename

app = Flask(__name__)
heroku = Heroku(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def results():
    fmt = request.args.get('format', 'csv')
    filename = 'results.{}'.format(fmt)

    response = make_response(rrr.results(request.files['file'], fmt))
    response.headers['Content-Type'] = mimetypes.guess_type(filename)[0]
    response.headers['Content-Disposition'] = (
        'attachment; filename={}'.format(filename)
    )
    return response


if __name__ == '__main__':
    app.debug = os.getenv('FLASK_DEBUG') or False
    app.run(port=8000)
