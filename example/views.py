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

from bson import ObjectId
from confu.ext.flask import ConfigurableBlueprint, route
from flask import Response, request

from diary import Diary


class WebDiary(ConfigurableBlueprint):
    needs = dict(ConfigurableBlueprint.needs, **{
        'diary': Diary,
    })

    @route('/')
    def note_index(self):
        return Response(str(self.diary.find()))

    @route('/<note_id>')
    def note_detail(self, note_id):
        return Response(str(self.diary.get(ObjectId(note_id))))


class WebEcho(ConfigurableBlueprint):
    @route('/')
    def echo(self):
        return Response(str(request.values))
