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

import pymongo
from confu import Configurable


class MongoDB(Configurable):
    defines = {
        'host': 'localhost',
        'port': 27017,
        'db_name': str,
    }
    conn = None

    def connect(self):
        self.conn = pymongo.Connection(host=self.host,
                                       port=self.port)

    @property
    def db(self):
        if not self.conn:
            self.connect()
        return self.conn[self.db_name]
