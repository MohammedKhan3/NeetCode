# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList
    while curr is not None:
        temp = curr.next
        while temp is not None and curr.value == temp.value:
            temp = temp.next
        curr.next = temp
        curr = temp
        
    return linkedList
