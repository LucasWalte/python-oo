"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

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
    def __init__(self, start=0):
        """Create a new generator, starting at the provided number."""
        self.start = start
        self.next = start

    def generate(self):
        """Return the next sequential number."""
        result = self.next
        self.next += 1
        return result

    def reset(self):
        """Reset the generator to the start number."""
        self.next = self.start

    def __repr__(self):
        """Return a string representation of the generator state."""
        return f"<SerialGenerator start={self.start} next={self.next}>"

