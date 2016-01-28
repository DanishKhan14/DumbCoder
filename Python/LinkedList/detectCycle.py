    def hasCycle(self, head):
        """
        The algorithm is of course Tortoise and hare.
        Here I do not check all the time whether we
        have reached the end but to handle it via an exception.

        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


        # Method 2:
        """
        If there is a cylce, fast will catch slow.
        Else, fast will reach None
        """

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
