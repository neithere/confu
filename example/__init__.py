#!/usr/bin/env python
#
#    Confu is a configuration management library.
#    Copyright © 2014  Andrey Mikhaylenko
#
#    This file is part of Confu.
#
#    Confu is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Confu is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Confu.  If not, see <http://gnu.org/licenses/>.

import argh
import flask

from db import MongoDB
from diary import Diary
from views import WebDiary, WebEcho


# configure application units for this site
mongo = MongoDB({'db_name': 'my_test'})
diary = Diary({'db': mongo.db})
web_diary = WebDiary({'diary': diary})
web_echo = WebEcho()


def create_wsgi_app():
    # Assemble a Flask app from multiple configurable units
    # (as opposed to the devel dedicated Flask apps that can be run
    #  as `webdiary serve` and `echo serve`).
    app = flask.Flask(__name__)
    app.register_blueprint(web_echo.blueprint, url_prefix='/echo')
    app.register_blueprint(web_diary.blueprint)
    return app


wsgi_app = create_wsgi_app()


# assemble CLI
parser = argh.ArghParser()
parser.add_commands([diary.find, diary.add])
parser.add_commands([web_diary.serve], namespace='webdiary')
parser.add_commands([web_echo.serve], namespace='echo')
parser.add_commands([wsgi_app.run])


if __name__ == '__main__':
    parser.dispatch()
