"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=99)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """
        Create SerialGenerator initializing with start value

        start: int
          value to start counting at and initialize back to on reset()

        counter: int
          value to store incremental value each time generate() function runs
        """
        self.start = start
        self.counter = start
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} counter={self.counter}>"

    def generate(self):
       "Increment current value of self.counter by 1"
       self.counter += 1
       return self.counter
    
    def reset(self):
        "Reset current value of self.counter back to self.start"
        self.counter = self.start
