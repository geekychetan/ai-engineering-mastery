from greet import greet


def test_greet_uses_the_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_is_a_string():
    assert isinstance(greet("world"), str)
