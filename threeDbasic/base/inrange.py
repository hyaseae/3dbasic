class inrange():
    """
    just some useful range things. idk already in python?
    """
    def __init__(self, start:float, end:float) -> None:
        if start > end:
            start, end = end, start
        self.start = start
        self.end = end
        self.range_length = end - start

    def get_length(self):
        """retutrns given range's length"""
        return self.range_length

    def check_value(self, value):
        """
        checks if value is in range.
        """
        return self.start <= value <= self.end
        
    def rerange(self, value, other):
        """
        rerange self's value to other range.
        """ 
        return other.start + (value - self.start) * (other.end - other.start) / (self.get_length())
    