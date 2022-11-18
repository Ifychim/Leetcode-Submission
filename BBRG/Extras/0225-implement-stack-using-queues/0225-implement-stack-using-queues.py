class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val=val
        self.next = next
        self.prev = prev
    
class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def insert(self, val):
        
        newNode = Node(val=val)
        
        #insert into empty list
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.head.prev, self.tail.next = None, None
            return
        
        else:
            self.tail.next = newNode
            newNode.prev, newNode.next = self.tail, None
            self.tail = newNode

            return
            
    def remove(self) -> int:
        
        #removing tail when it is also the head
        if self.tail == self.head:
            res = self.tail.val
            
            self.head.next, self.tail.next = None, None
            self.head.prev, self.tail.prev = None, None
            self.head, self.tail = None, None
            
            return res
        
        elif self.tail:
            res = self.tail.val
            
            temp = self.tail.prev
            
            self.tail.next, self.tail.prev = None, None
            self.tail = None
            
            self.tail = temp
            
            return res
    
class MyStack:

    def __init__(self):
        self.stack = LinkedList()

    def push(self, x: int) -> None:
        self.stack.insert(x)

    def pop(self) -> int:
        return self.stack.remove()
    
    def top(self) -> int:
        return self.stack.tail.val

    def empty(self) -> bool:
        
        if not self.stack.head:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()