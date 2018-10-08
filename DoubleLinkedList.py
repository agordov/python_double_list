class Node():
    """Class for node that are stored in doubleLinkedList"""
    def __init__(self, value=None, prev=None, next_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev


class DoubleLinkedList():
    """This class realize DoubleLinkedList"""

    def __init__(self, collection=None):
        self._head = None
        self._tail = None
        self._size = 0
        if collection is not None:
            for it in collection:
                self.push_back(it)

    def push_front(self, value):
        """Add value to front"""
        if self._head is None:
            self._head = self._tail = Node(value)
        else:
            self._head.prev = Node(value)
            self._head.prev.next = self._head
            self._head = self._head.prev
        self._size += 1

    def push_back(self, value):
        """Add value to back"""
        if self._head is None:
            self.push_front(value)
        else:
            self._tail.next = Node(value)
            self._tail.next.prev = self._tail
            self._tail = self._tail.next
            self._size += 1

    def pop_back(self):
        """Delete last element"""
        if self._tail is None:
            # raise IndexError((': {class_name}.{method_name}(x): {what}'.format(
            #     class_name='DoubleLinkedList',
            #     method_name='pop_back',
            #     what='deletion from non initialized list'
            #     )))
            raise IndexError
        if self.size() == 1:
            self.clear()
        else:
            self._tail.prev.next = None
            self._tail = self._tail.prev
            self._size -= 1

    def pop_front(self):
        """Delete first element"""
        if self._head is None:
            # raise IndexError((': {class_name}.{method_name}(x): {what}'.format(
            #     class_name='DoubleLinkedList',
            #     method_name='pop_front',
            #     what='deletion from non initialized list'
            #     )))
            raise IndexError
        if self.size() == 1:
            self.clear()
        else:
            self._head.next.prev = None
            self._head = self._head.next
            self._size -= 1

    def front(self):
        """Return first element"""
        if self._head is None:
            return None
        return self._head.value

    def back(self):
        """Return last value"""
        if self._head is None:
            return None
        return self._tail.value

    def empty(self):
        """Check if list is empty"""
        return self._head is None

    def size(self):
        """Return size of list"""
        return self._size

    def clear(self):
        """Clear list"""
        self._head = self._tail = None
        self._size = 0

    def insert(self, value, index):
        """Insert element via index"""
        if index == 0:
            self.push_front(value)
        elif index >= self.size() or index < 0:
            # raise IndexError((': {class_name}.{method_name}(x): {what}'.format(
            #     class_name='DoubleLinkedList',
            #     method_name='insert',
            #     what='index out of range'
            #     )))
            raise IndexError
        else:
            current_node = self._head
            cur_ind = 0
            while cur_ind < index and current_node is not None:
                current_node = current_node.next
                cur_ind += 1
            new_node = Node(value)
            new_node.next = current_node
            new_node.prev = current_node.prev
            current_node.prev.next = new_node
            current_node.prev = new_node
            self._size += 1

    def contains(self, key):
        """Check if list contain key value"""
        current_node = self._head
        while current_node is not None:
            if current_node.value == key:
                return True
            else:
                current_node = current_node.next
        return False

    def delete(self, key):
        """Delete from list by key value"""
        if not self.contains(key):
            # raise ValueError(': {class_name}.{method_name}(x): {what}'.format(
            #     class_name='DoubleLinkedList',
            #     method_name='delete',
            #     what='x not in list'
            #     ))
            raise ValueError
        current_node = self._head
        while current_node is not None:
            if current_node.value == key:
                if current_node == self._head:
                    current_node = current_node.next
                    self.pop_front()
                    continue
                elif current_node == self._tail:
                    current_node = current_node.next
                    self.pop_back()
                    continue
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    self._size -= 1
            current_node = current_node.next

    def to_list(self):
        """Transform DoubleLinkedList to [] list"""
        output = [0] * self._size
        i = 0
        current_node = self._head
        while current_node is not None:
            output[i] = current_node.value
            i += 1
            current_node = current_node.next
        return output

    def get_item(self, index):
        """Get value from list by index"""
        if index >= self.size() or index < 0:
            # raise IndexError((': {class_name}.{method_name}(x): {what}'.format(
            #     class_name='DoubleLinkedList',
            #     method_name='insert',
            #     what='index out of range'
            # )))
            raise IndexError
        current_node = self._head
        i = 0
        while i < index:
            current_node = current_node.next
        return current_node.value


if __name__ == '__main__':
    l = DoubleLinkedList()
    print(l.to_list())
    l = DoubleLinkedList([1, 2, 3])
    print(l.to_list())
    l.delete(1)
    print(l.size())
    print(l.to_list())
