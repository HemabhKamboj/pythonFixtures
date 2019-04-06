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

def test_hemabh_data(db):
    hemabh_data = db.get_data('Hemabh')
    assert hemabh_data['id'] == 1
    assert hemabh_data['name'] == 'Hemabh'
    assert hemabh_data['result'] == 'pass'
    assert hemabh_data['branch'] == 'IT'

def test_dhruv_data(db):
    dhruv_data = db.get_data('Dhruv')
    assert dhruv_data['id'] == 2
    assert dhruv_data['name'] == 'Dhruv'
    assert dhruv_data['result'] == 'fail'
    assert dhruv_data['branch'] == 'CSE'







