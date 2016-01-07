#!/usr/bin/python

class Node():
    def __init__(self, key):
        self.data = key
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,data):
        self.data = data

    def setNext(self,nextItem):
        self.next = nextItem

class ULinkedList():
    '''
    this is unordered linked list. Here items are added in the beginning
    '''
    def __init__(self):
        self.head = None

    def addNode(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count

    def search(self, key):
        current = self.head
        found = False
        while current is not None or found is True:
            if current.getData() == key:
                found = True
            else:
                current = current.getNext()

        return found

    def removeNode(self, key):
        previous = None
        current = self.head
        found = False
        while current is not None or found is True:
            if current.getData() == key:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext() == current.getNext()

        return found

    def reverseList(self):
        """
        :return: Node
        """
        current = self.head
        new_head = None
        while current:
            temp = current.getNext()
            current.setNext = new_head
            new_head = current
            current = temp
        return new_head


    def reverseBetween(self, head, m, n):
        if m >= n:
            return head
        #Step 1#
        ohead = dummy = Node(0)
        whead = wtail = head
        dummy.next = head
        for i in range(n-m):
            wtail = wtail.next
        #Step 2#
        for i in range(m-1):
            ohead, whead, wtail = whead, whead.next, wtail.next
        #Step 3#
        otail, wtail.next = wtail.next, None
        revhead, revtail = self.reverse(whead)
        #Step 4#
        ohead.next, revtail.next = revhead, otail
        return dummy.next

    def reverse(self, head):
        pre, cur, tail = None, head, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre, tail


class OLinkedList():
    '''
    this is ordered linked list. here elements are ordered based on
    some condition. in this particular implementatio, we are imple-
    -menting sorted linked list.
    '''
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        found = False
        previous = None
        while current is not None and found is False:
            if current.getData() >= item:
                found = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, key):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.getData() == key:
                found = True
            elif current.getData() > key:
                stop = True
            else:
                current = current.getNext()

        return found

olist = OLinkedList()
ulist = ULinkedList()
for i in range(10):
    ulist.addNode(i)

olist.add(34)
olist.add(23)
olist.add(12)
olist.add(29)
olist.add(9)

print ulist.size()
print olist.search(34)

