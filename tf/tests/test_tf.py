from tf import base

def test_tf():
    val1, val2 = 1, 2
    result = base.friendlyfunc(val1, val2)
    assert result == 3
