#!/usr/bin/python

    def addTwoNumbers(self, l1, l2):
        """
        Note that numbers are stored in reverse order in l1 and l2.
        This means, if last digit as carry forward needs to be added,
        we can add that in the end.

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Method 1: Iterative
        carry = 0
        res = n = ListNode(0);
        while l1 or l2 or carry: # or carry condition will take care of the last digit in the end until its 0
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10) #
            n.next = n = ListNode(val)
        return res.next

        # Method 2: Recursive
            # Method 2: Recursive

        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        a = l1.val + l2.val
        p = ListNode(a%10)
        p.next = self.addTwoNumbers(l1.next, l2.next)
        if (a>=10):
            p.next = self.addTwoNumbers(p.next, ListNode(1))
        return p
