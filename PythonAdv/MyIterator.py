class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Stop iteration when the condition is met
        value = self.current
        self.current += 1  # Move to the next value
        return value

# Creating an instance of MyIterator
obj = MyIterator(6, 10)

# Using for loop (internally calls iter() and next())
for num in obj:
    print(num)
