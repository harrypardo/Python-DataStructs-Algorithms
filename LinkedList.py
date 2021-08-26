class Node:
    """An object for stroring
    Models two attributes - data
    """
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def __repr__(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
        return ''

    def add_to_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def add_to_nth(self, data, n):
        if n == 0:
            self.add_to_head(data)
            return
        if n == self.count:
            self.add_to_tail(data)
            return

        ptr = self.head
        count = 0
        last_ptr = ptr
        new_node = Node(data)
        while ptr:
            if count == n:
                last_ptr.next = new_node
                new_node.next = ptr
                break
            count += 1
            last_ptr = ptr
            ptr = ptr.next
        self.count += 1

    def remove_from_head(self):
        if not self.head: return
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data

    def remove_nth(self, n):
        if n == 0:
            return self.remove_from_head()
        count = 0
        ptr = self.head
        last_ptr = ptr
        while ptr:
            if count == n:
                data = ptr.data
                last_ptr.next = ptr.next
                self.count -= 1
                if count == self.count:
                    self.tail = last_ptr
                return data
            count += 1
            last_ptr = ptr
            ptr = ptr.next
        return None


ll_list = SinglyLinkedList()
ll_list.add_to_tail(6)
ll_list.add_to_head(1)
ll_list.add_to_head(2)
ll_list.add_to_tail(3)
ll_list.add_to_head(5)
ll_list.add_to_tail(4)
ll_list.add_to_nth(5555, 0)
print(ll_list)

print('----')
ll_list.remove_nth(3)

print(ll_list)

