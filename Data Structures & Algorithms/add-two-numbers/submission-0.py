class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add digits + carry
            total = val1 + val2 + carry

            # Current digit
            digit = total % 10

            # Carry
            carry = total // 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move forward
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
        