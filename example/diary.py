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


class Diary(Configurable):
    defines = {
        'db': pymongo.database.Database,
        'collection_name': 'my_diary',
    }

    def init(self):
        self.collection = self.db[self.collection_name]

    def find(self):
        return list(self.collection.find())

    def get(self, note_id):
        return self.collection.find_one({'_id': note_id})

    def add(self, note):
        return self.collection.insert({'note': note})
