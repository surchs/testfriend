def friendlyfunc(value, addition):
    return value + addition


def other_func(word, addition):
    if isinstance(word, str):
        return ' '.join((word, addition))
    else:
        return friendlyfunc(word, addition)