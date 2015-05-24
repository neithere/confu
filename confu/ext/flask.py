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

import os

from flask import Flask, Blueprint
from confu import Configurable


def route(url_rule):
    def decorate(func):
        func._url_rule = url_rule
        return func
    return decorate


class ConfigurableBlueprint(Configurable):
    """
    A Flask-specific configurable unit.

    When configured, initializes a Blueprint with pre-declared routing
    and provides a dedicated `serve` method (which is also a CLI command)
    to debug this blueprint on its own.
    """
    needs = {
        'debug': bool(os.environ.get('DEBUG', False)),
    }

    def init(self):
        # create an configurable-bound blueprint
        # with our methods pre-declared as views
        self.blueprint = Blueprint(self.__class__.__name__, __name__)
        for attr in dir(self):
            meth = getattr(self, attr)
            url_rule = getattr(meth, '_url_rule', None)
            if url_rule:
                self.blueprint.route(url_rule)(meth)

    def serve(self):
        # ad-hoc dedicated devel app for this blueprint
        app = Flask(__name__)
        app.register_blueprint(self.blueprint)
        app.run(debug=self.debug)
