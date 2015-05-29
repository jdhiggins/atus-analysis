from atus_analysis import *

def test_replace_code():
    assert replace_code('500199') == 'Data codes, n.e.c.*'


def test_replace_fips():
    assert replace_fips(10) == 'DE'

