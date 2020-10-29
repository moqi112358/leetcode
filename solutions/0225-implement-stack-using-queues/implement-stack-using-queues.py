# Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).
#
# Implement the MyStack class:
#
#
# 	void push(int x) Pushes element x to the top of the stack.
# 	int pop() Removes the element on the top of the stack and returns it.
# 	int top() Returns the element on the top of the stack.
# 	boolean empty() Returns true if the stack is empty, false otherwise.
#
#
# Notes:
#
#
# 	You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
# 	Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.
#
#
# Follow-up: Can you implement the stack such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
#
#  
# Example 1:
#
#
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
#
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
#
#
#  
# Constraints:
#
#
# 	1 <= x <= 9
# 	At most 100 calls will be made to push, pop, top, and empty.
# 	All the calls to pop and top are valid.
#
#


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            self.queue1.append(x)
        elif len(self.queue1) != 0:
            self.queue1.append(x)
        elif len(self.queue2) != 0:
            self.queue2.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.queue1) != 0:
            while len(self.queue1) != 1:
                tmp = self.queue1.pop(0)
                self.queue2.append(tmp)
            tmp = self.queue1.pop(0)
            return tmp
        elif len(self.queue2) != 0:
            while len(self.queue2) != 1:
                tmp = self.queue2.pop(0)
                self.queue1.append(tmp)
            tmp = self.queue2.pop(0)
            return tmp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.queue1) != 0:
            return self.queue1[-1]
        if len(self.queue2) != 0:
            return self.queue2[-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
