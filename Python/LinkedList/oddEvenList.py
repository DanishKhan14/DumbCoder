    def oddEvenList(self, head):
        """
          Have a pointer for the beginning of odd and a pointer for beginning of even,
          then we have a odd pointer that points the current odd node and use it to
          connect to its oddPointer.next.next, same goes for connecting even. When even
          pointer is null we know it's at the end of the list. Then we just merge two list
          and return odd head.

        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd,p=head,head.next
        while p and p.next:
            odd.next,p.next.next,p.next=p.next,odd.next,p.next.next #insert
            odd,p=odd.next,p.next
        return head

        # Method 2:

        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next