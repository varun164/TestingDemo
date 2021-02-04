import pytest

import addsub


@pytest.mark.parametrize('a,b,res', [(5, 4, 9), (10, 20, 30), ('pf', 'sd', 'pfsd')])
#@pytest.mark.skip
def test_add(a, b, res):
    #assert addsub.add(5, 4) == 6
    #assert addsub.add(5, 5) == 10
    assert addsub.add(a, b) == res

# @pytest.mark.skip(reason= "skip sub")
#def test_sub():
 #   assert addsub.sub(8, 4) == 4
  #  assert addsub.sub(9, 9) == 0


# @pytest.mark.skipif(4>3,reason="four is greaterthan three")
#def test_add_strings():
 #   c = addsub.add('pf', 'sd')
  #  assert c == 'pfsd'
   # assert type(c) is str
    #print("Concatenated string is", c)
