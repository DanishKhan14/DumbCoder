    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        #Method 1: Using O(n) extra space

        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next

        # Method 2: Using O(1) space

    def partition(self, head, x):
        #create a new head to make the iteration easier
        newHead =ListNode(-1)
        newHead.next = head
        cur = head
        #"pre" is the node ahead of "cur"
        pre = newHead
        #"last" is the last node that smaller than x so far
        last = newHead
        while cur:
            if cur.val < x:
                #if "pre" is "last", it means we haven't done any partition yet, so we do not need to do anything
                if pre == last:
                    pre = pre.next
                    last = last.next
                    cur = cur.next
                #move the "cur" to the end of "last" and update "last" and "cur"
                else:
                    tmp = last.next
                    pre.next = cur.next
                    last.next = cur
                    cur.next = tmp
                    last = last.next
                    cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return newHead.next


    # Method 3: Recursive

    def partition(self, head, x):
        if not head or not head.next:
            return head
        cur = head
        nextp = self.partition(head.next, x)
        cur.next = nextp
        if cur.val >= x:
            if nextp and nextp.val <x:
                head = nextp
                while nextp.next and nextp.next.val < x:
                    nextp = nextp.next
                cur.next = nextp.next
                nextp.next = cur
        return head
