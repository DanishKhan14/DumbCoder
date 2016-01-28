

    # Method 1

    def getIntersectionNode(self, headA, headB):
        """
        Maintain two pointers in the lists under the constraint that both
        lists have the same number of nodes starting from the pointers.
        We need to calculate the length of each list though. So O(N) for time and O(1) for space.

        :param self:
        :param headA:
        :param headB:
        :return:
        """
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA


    # Method 2:

        if not headA or not headB:return None
        a,b=headA,headB
        while a or b:
            if not a:   a=headB
            if not b:   b=headA
            if a is b: return a
            a , b = a.next,b.next
