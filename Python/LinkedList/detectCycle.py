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

    def detectAndReturnCycle(self, head):
        """
        # This explanation is taken from dashang's post.

        Consider the following linked list, where E is the cylce entry and X, the crossing point of fast and slow.
        H: distance from head to cycle entry E
        D: distance from E to X
        L: cycle length
                          _____
                         /     \
        head_____H______E       \
                        \       /
                         X_____/


        If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D).
        Assume fast has traveled n loops in the cycle, we have:
        2H + 2D = H + D + L  -->  H + D = nL  --> H = nL - D
        Thus if two pointers start from head and X, respectively, one first reaches E, the other also reaches E.
        In my solution, since fast starts at head.next, we need to move slow one step forward in the beginning of part 2


        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else: # if there is an exception, we reach the end and there is no cycle
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
