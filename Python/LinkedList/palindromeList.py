# O(n) time and  O (1) space

    def isPalindrome(self, head):
        """
        Find the middle node. Reverse second half of ll.
        Compare the first and second half. It should
        be same.

        :type head: ListNode
        :rtype: bool
        """
        # Method 1
        ---------

        if head is None or head.next is None:
            return True
        slow, fast = head, head.next
        while slow and fast and fast.next: # fast and fast.next both should not be None
            slow = slow.next
            fast = fast.next.next
        revhead = self.reverseO(slow.next)
        slow.next = None
        while head and revhead:
            if (head.val == revhead.val):
                head, revhead = head.next, revhead.next
            else:
                return False
        return True

    def reverseO(self, head):
        if head is None or head.next is None:
            return head
        pre = None
        while head:
            head.next, pre, head = pre, head, head.next
        return pre

        # Method 2: O(n) space
        -----------

        vals = []
        while head:
            vals += head.val,
            head = head.next
        return vals == vals[::-1]

        # Method 3: Recursion
        ---------------------

        if not head or not head.next: return True
        if not head.next.next:
            if head.val==head.next.val:return True
            return False
        length=0
        headCopy=head
        while headCopy:
            length+=1
            headCopy=headCopy.next
        return self.comp(head,length,0)

    def comp(self,node,length,i):
        if i==(length-1)/2:
            if length%2==1: return node.next
            else:
                if node.val==node.next.val:
                    return node.next.next
                else:
                    return False
        counterNode=self.comp(node.next,length,i+1)
        if not counterNode:
            return False
        if node.val==counterNode.val:
            if i==0: return True
            return counterNode.next
        return False