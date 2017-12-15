"""TBD"""


class Handler:
    """TBD"""

    def __init__(self):
        """TBD"""
        pass

    def __del__(self):
        """TBD"""
        pass

    def to_pattern(self, symbol):
        """TBD"""
        # Definition of patterns
        symbol_to_pattern = {
            # Numbers
            "0": [1, 1, 1, 1, 1, 1, 0],
            "1": [0, 1, 1, 0, 0, 0, 0],
            "2": [1, 1, 0, 1, 1, 0, 1],
            "3": [1, 1, 1, 1, 0, 0, 1],
            "4": [0, 1, 1, 0, 0, 1, 1],
            "5": [1, 0, 1, 1, 0, 1, 1],
            "6": [1, 0, 1, 1, 1, 1, 1],
            "7": [1, 1, 1, 0, 0, 0, 0],
            "8": [1, 1, 1, 1, 1, 1, 1],
            "9": [1, 1, 1, 1, 0, 1, 1],
            # Characters (big)
            "A": [1, 1, 1, 0, 1, 1, 1],
            "C": [1, 0, 0, 1, 1, 1, 0],
            "E": [1, 0, 0, 1, 1, 1, 1],
            "H": [0, 1, 1, 0, 1, 1, 1],
            "I": [0, 0, 0, 0, 1, 1, 0],
            "L": [0, 0, 0, 1, 1, 1, 0],
            "O": [1, 1, 1, 1, 1, 1, 0],
            "P": [1, 1, 0, 0, 1, 1, 1],
            "S": [1, 0, 1, 1, 0, 1, 1],
            "U": [0, 1, 1, 1, 1, 1, 0],
            # Characters (small)
            "b": [0, 0, 1, 1, 1, 1, 1],
            "c": [0, 0, 0, 1, 1, 0, 1],
            "d": [0, 1, 1, 1, 1, 0, 1],
            "h": [0, 0, 1, 0, 1, 1, 1],
            "l": [0, 0, 0, 0, 1, 1, 0],
            "n": [0, 0, 1, 0, 1, 0, 1],
            "o": [0, 0, 1, 1, 1, 0, 1],
            "r": [0, 0, 0, 0, 1, 0, 1],
            "u": [0, 0, 1, 1, 1, 0, 0],
        }
        # Check symbol type
        if(not isinstance(symbol, str)):
            raise TypeError
        # Convert character to pattern
        try:
            pattern = symbol_to_pattern[symbol]
        except KeyError:
            raise KeyError("Invalid symbol")
        # Return
        return pattern
