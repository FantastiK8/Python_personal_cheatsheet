class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.get_data()
            self.current = self.current.get_next()
            return item
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

        
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def add(self, item, next): 
        new_node = Node(item, None)
        new_node.next(self.head)
        self.head = new_node


test_list = LinkedList()
test_list.add(1, None)
test_list.add(2, None)
test_list.add(3, None)
for item in test_list:
    print(item)