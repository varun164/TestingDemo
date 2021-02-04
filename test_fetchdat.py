from fetchdata import Emp
import pytest
db = None
@pytest.fixture(scope='module')
def dbcnct():
    print("setup module")
    db=Emp()
    db.connect('emp.json')
    yield db
    print("tear_down module")
def test_Sandhya_data(dbcnct):
    d = dbcnct.retrievedata('Sandhya')
    assert d['eid'] == 45697
    assert d['name'] == 'Sandhya'


def test_shekhar_data(dbcnct):
    d = dbcnct.retrievedata('shekhar')
    assert d['eid'] == 5164
    assert d['name'] == 'shekhar'

def teardown_module():
    print("closed")