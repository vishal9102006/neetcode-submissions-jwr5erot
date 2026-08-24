class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}

        # 1. Create a new node for every original node
        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # 2. Connect next and random pointers
        current = head

        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)

            current = current.next

        return old_to_new[head]