from basecamp_sandbox import greet, reverse_string


def test_greet_includes_the_name():
    assert greet("Ada") == "Hello, Ada!"


def test_reverse_string_of_empty_string_is_empty():
    assert reverse_string("") == ""


def test_reverse_string_leaves_single_character_unchanged():
    assert reverse_string("a") == "a"


def test_reverse_string_leaves_palindrome_unchanged():
    assert reverse_string("racecar") == "racecar"


def test_reverse_string_reverses_ascii():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_reverses_precomposed_non_ascii():
    assert reverse_string("héllo") == "olléh"


def test_reverse_string_twice_returns_original():
    text = "Hello, world!"
    assert reverse_string(reverse_string(text)) == text


def test_reverse_string_splits_combining_mark_from_its_base():
    # Pins the code-point limitation: decomposed "é" is "e" + U+0301.
    assert reverse_string("é") == "́e"
