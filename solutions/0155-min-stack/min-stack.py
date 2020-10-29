# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#
# 	push(x) -- Push element x onto stack.
# 	pop() -- Removes the element on top of the stack.
# 	top() -- Get the top element.
# 	getMin() -- Retrieve the minimum element in the stack.
#
#
#  
# Example 1:
#
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
#  
# Constraints:
#
#
# 	Methods pop, top and getMin operations will always be called on non-empty stacks.
#
#


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        tmp = self.getMin()
        if tmp is None or x < tmp:
            tmp = x
        self.stack.append((x,tmp))
        return
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        return
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
