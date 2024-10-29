# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    '''
    Understand:
    Two pointer approach -> slow and fast pointer
    Both start at same point but fast pointer moves fast
    until the fast.next is not null in that way we will have 
    slow at the middle.
    and head is always there.
    
    '''
    # Write your code here.
    s=linkedList
    f = linkedList
    while f and f.next:
        s = s.next
        f = f.next.next
    return s
