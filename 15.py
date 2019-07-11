def node_reverse(head):
    pre = None
    while(head):
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre
