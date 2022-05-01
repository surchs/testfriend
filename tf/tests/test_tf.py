from tf import base

def test_tf():
    val1, val2 = 1, 2
    result = base.friendlyfunc(val1, val2)
    assert result == 3


def test_otherfunc():
    word1, word2 = 'hello', 'world'
    result = base.other_func(word1, word2)
    assert result == 'hello world'