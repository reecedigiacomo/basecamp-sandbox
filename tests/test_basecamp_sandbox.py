from basecamp_sandbox import greet


def test_greet_includes_the_name():
    assert greet("Ada") == "Hello, Ada!"
