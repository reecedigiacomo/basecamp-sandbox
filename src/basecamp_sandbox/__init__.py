def greet(name: str) -> str:
    return f"Hello, {name}!"


def reverse_string(text: str) -> str:
    # shortcut: reverses by code point, so combining marks and joined emoji (ZWJ
    # sequences, flags) get split apart. Upgrade to grapheme-cluster reversal if
    # user-facing text needs it.
    return text[::-1]
