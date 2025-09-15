class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def createList(l=[]):
    if not l:
        return None
    head = node(l[0])
    current = head
    for i in l[1:]:
        current.next = node(i)
        current = current.next
    return head


def printList(H):
    current = H
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


def mergeOrderesList(p, q):
    dummy = node(0)
    tail = dummy

    while p and q:
        if p.data <= q.data:
            tail.next = node(p.data)
            p = p.next
        else:
            tail.next = node(q.data)
            q = q.next
        tail = tail.next

    # Append remaining elements
    while p:
        tail.next = node(p.data)
        p = p.next
        tail = tail.next
    while q:
        tail.next = node(q.data)
        q = q.next
        tail = tail.next

    return dummy.next


#################### FIX command ####################
# Input parsing
input_data = input("Enter 2 Lists : ")
L1_str, L2_str = input_data.strip().split()
L1 = list(map(int, L1_str.split(',')))
L2 = list(map(int, L2_str.split(',')))

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(m)
