class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
            
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()