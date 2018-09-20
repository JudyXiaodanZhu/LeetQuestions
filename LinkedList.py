"""
Reverse Linked List II
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in xrange(m-1):
            pre = pre.next
        cur = start = pre.next
        # reverse the defined part 
        node = None
        for _ in xrange(n-m+1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur= nxt
        # connect three parts
        start.next = cur
        pre.next = node
        return dummy.next

"""
Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
"""
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = entry = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return None

"""
Reorder List
Given 1->2->3->4, reorder it to 1->4->2->3.
"""
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr = slow.next
        slow.next = None
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        while head and prev:
            temp = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp
            head = temp
            prev = temp2

"""
Sort List
Input: 4->2->1->3
Output: 1->2->3->4
"""
    def sortList(self, head):
        if not head or not head.next: return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)
    
    # merge in-place without dummy node        
    def merge(self, l, r):
        if not l or not r: return l or r
        if l.val > r.val:
            r, l = l, r
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        pre.next = l or r
        return head