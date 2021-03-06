from math_func import StudentDB
import pytest

@pytest.fixture(scope='module')
def db():
    print('----------setup----------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('----------teardown----------------')
    db.close()

def test_scott_data(db):
    scott_data = db.get_data('Hemabh')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Hemabh'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):
    mark_data = db.get_data('Dhruv')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Dhruv'
    assert mark_data['result'] == 'fail'