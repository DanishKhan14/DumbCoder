# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Method 1: Recursive. To Down
    #More intuitive but O(nlog n) time complexity
    # and O(logn) recursive stack space

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root

        # Method 2: O(n) Time  Bottom Up

        """
        1) Get the Middle of the linked list and make it root.
        2) Recursively do same for left half and right half.
            a) Get the middle of left half and make it left child of the root
            created in step 1.
            b) Get the middle of right half and make it right child of the
            root created in step 1.
        """