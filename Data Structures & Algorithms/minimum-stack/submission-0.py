class MinStack:
    # You might think, cant we just simply use an array?
    # We infact can! Buuuuut we need to do a bit more because there is a problem... 
    # Remember we need to be able to get the min
    # Now.. we could store this min as just some variable inside the class.. 
    # But if we have a min say -2.. and then we add -3 to the stack, that becomes the new min
    # You might think to just update the current min variable.. The issue comes when we
    # eventually remove -3.... the new min is supposed to be -2 at that point
    # But if we used a simple variable, we would have lost track of -2

    # What if we just stored every value as a tuple where x is the actual value,
    # and y is the current min.
    # That way, no matter what we remove, we know who the last min was



    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        
        top = self.stack[-1]
        if val <= top[1]: # If the new value is smaller than the the current min
            self.stack.append((val, val)) # Store this as the new min
        else:
            self.stack.append((val, top[1])) # If not, then store the new val and keep y as the existing min
        

    # ===============# We are guaranteed that these will only be called on a non-empty stack===========
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] # Get x from the topmost element
        
    def getMin(self) -> int:
        return self.stack[-1][1] # Get y from the topmost element.... Remember the y for all elements will be the current min
