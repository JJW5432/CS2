from gutenberg import *

def test_strip_punctauation():
    assert is_letter('a')
    assert is_letter('Z')
    assert not is_letter('4')
    assert not is_letter (',')
    assert strip_punctuation('foo') == 'foo'
    assert strip_punctuation('foo,') == 'foo'
    assert strip_punctuation(' !%32foo(*&#2 $$') == 'foo'
