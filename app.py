#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mimetypes
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
    fmt = request.form.get('format', 'csv')
    pdf = request.files['file']
    filename = '{}-results.{}'.format(pdf.filename[:-4], fmt)

    response = make_response(rrr.results(pdf, fmt))
    response.headers['Content-Type'] = mimetypes.guess_type(filename)[0]
    response.headers['Content-Disposition'] = (
        'attachment; filename={}'.format(filename)
    )
    return response


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
