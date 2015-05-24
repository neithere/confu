from confu import Configurable
from monk import ValidationError
import pytest


def test_missing_key():
    class C(Configurable):
        needs = {'foo': int}
    with pytest.raises(ValidationError) as e:
        C()
    assert 'value must be int' in str(e)


def test_validate_type():
    class C(Configurable):
        needs = {'foo': int}
    C({'foo': 1})
    with pytest.raises(ValidationError) as e:
        C({'foo': 'bar'})
    assert 'value must be int' in str(e)


def test_defaults():
    class C(Configurable):
        needs = {'foo': 1}
    c = C()
    assert c['foo'] == 1
    assert c.foo == 1


def test_extra():
    class C(Configurable):
        needs = {'foo': 1, 'bar': 'quux'}

    # defaults
    assert C().foo == 1

    # basic config only
    assert C({'foo': 2}).foo == 2
    assert C({'foo': 2}, {}).foo == 2

    # extra config only
    assert C({}, {'foo': 2}).foo == 2
    assert C(None, {'foo': 2}).foo == 2

    # extra config overrides basic
    assert C({'foo': 2}, {'foo': 3}).foo == 3

    # basic + extra merged
    c = C({'foo': 2, 'bar': 'gumby'}, {'bar': 'albatross'})
    assert c.foo == 2
    assert c.bar == 'albatross'
