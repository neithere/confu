# coding: utf-8
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

"""
~~~~~
Confu
~~~~~
"""
# TODO ENV vars to conf
try:
    from monk import validate, merge_defaults
except ImportError:
    # monk < 0.13
    from monk.validation import validate
    from monk.manipulation import merge_defaults
from monk.modeling import DotExpandedDict


__version__ = '0.0.2'


class Configurable(DotExpandedDict):
    """
    A functional unit that can be configured in a specific way.

    Example::

        class Diary(Configurable):
            needs = {
                'db': pymongo.database.Database,
                'tz': 'Europe/Prague',
            }

            def log(self, note):
                self.db.insert({
                    'note': note,
                    'time': datetime.datetime.utcnow(),
                    'tz': self.tz,
                })

        db = ...
        diary = Diary({'db': db})
        diary.log('hello')

    In this example the `Diary` instance, when created, will:

    1. insert default values instead of missing ones;
    2. validate the resulting configuration to detect missing/unknown keys,
       invalid data types, etc.;
    3. update inner dictionary with the configuration variables;
    4. call the `init()` method.

    Note that `Configurable` is a dictionary subclass (with dot-expanded
    interface for cleaner code), so this works fine::

        class Foo(Configurable):
            needs = {
                'bar': 123,
            }

        foo = Foo()
        assert foo['bar'] == foo.bar == 123

        foo = Foo({'bar': 456})
        assert foo['bar'] == foo.bar == 456

    .. note::  On environment variables

        Please note that default values are used to guess the setting's data
        type.  Consider this code::

            class Foo(Configurable):
                needs = {
                    'debug': os.environ.get('DEBUG', False)
                }

        It works.  But what's wrong with it?

        The ``os.environ.get('DEBUG', False)`` expression returns a `str` if
        the environment variable `DEBUG` exists and a `bool` if it doesn't.
        This is **wrong** because you get inconsistent schema against which
        the unit configuration will be validated.

        Always make ensure that the default value is of a certain type, e.g.::

            class Foo(Configurable):
                needs = {
                    'debug': bool(os.environ.get('DEBUG', False))
                }

        Also note that ``DEBUG=0`` is also a string and ``bool('0') == True``.

    """
    needs = {}

    def __init__(self, conf=None):
        conf = conf or {}
        merged = merge_defaults(self.needs, conf)
        validate(self.needs, merged)
        self.update(merged)
        self.init()

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self))

    def init(self):
        pass
