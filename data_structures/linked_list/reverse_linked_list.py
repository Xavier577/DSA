from linked_list import create_linked_list

ll = create_linked_list([1, 2, 3, 4, 5])


def reverse_linked_list(linked_list):
    # code goes here
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

    return linked_list


print(ll.values())
print(reverse_linked_list(ll).values())
