"""TBD"""

from SevenSegs import Handler


def setup_function():
    """TBD"""
    global tst_handler
    # Create handler
    tst_handler = Handler()


def teardown_function():
    """TBD"""
    global tst_handler
    # Delete handler
    del tst_handler


def test_object_creation():
    """TBD"""
    # Assert handler
    assert isinstance(tst_handler, object)


def test_return_type():
    """TBD"""
    # Assign pattern
    pattern = tst_handler.to_pattern("1")
    # Assign pattern type
    assert isinstance(pattern, list)


def test_return_length():
    """TBD"""
    # Assign pattern
    pattern = tst_handler.to_pattern("1")
    # Assign pattern length
    assert 7 == len(pattern)


def test_every_symbol():
    """TBD"""
    # Define all symbols
    symbols = [
        ["0", [1, 1, 1, 1, 1, 1, 0]],
        ["A", [1, 1, 1, 0, 1, 1, 1]],
        ["b", [0, 0, 1, 1, 1, 1, 1]],
    ]
    # Iterate each character
    for value, pattern in symbols:
        # Assert every pattern
        assert pattern == tst_handler.to_pattern(value)
