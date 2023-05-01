# insert element at end

# create a node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linklist:
    def __init__(self):
        self.head = None
# inset node at beginning

    def insert_in_list(self, data, k):
        if k == "start":
            node_object = Node(data, self.head)
            self.head = node_object
        elif k == "end":
            node_object = Node(data)
            if self.head == None:
                self.head = node_object
                return
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = node_object
        elif isinstance(k, int):

            if k != 0:
                node_object = Node(data)
                n = ll.head
                i = 1
                while i < k:
                    n = n.next
                    i += 1
                node_object.next = n.next
                n.next = node_object
            elif k == 0:
                node_object = Node(data)
                node_object.next = ll.head
                ll.head = node_object

    def del_element(self, i):
        j = 1
        n = ll.head
        if i == 1:
            ll.head = ll.head.next
        else:
            cur_node = ll.head
            # while j < i-1:
            #     d = d.next
            #     j += 1
            # d.next = d.next.next
            # return
            while cur_node and j < i:
                prev = cur_node
                cur_node = cur_node.next
                j += 1

            if cur_node == None:
                # if this executed that means element that we want to delete is not present in list
                return
            prev.next = cur_node.next
            cur_node = None

# to delete key or particular value
    def del_value(self, key):
        cur_node = self.head
    # this check if element to be deleted is first element.
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        # loop to extract through the linked list
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        prev.next = cur_node.next
        cur_node = None
        if cur_node == None:
            # if this executed that means element that we want to delete is not present in list
            return

    def pri(self):
        n = self.head
        llstr = ''
        while n:
            llstr += str(n.data)+" --> "
            n = n.next
        print(llstr)


ll = Linklist()
ll.insert_in_list(4, "start")
ll.insert_in_list(5, "start")
ll.insert_in_list(6, 1)
ll.insert_in_list(422, "end")
ll.insert_in_list(5432, 1)
ll.insert_in_list(111, 0)
ll.pri()
ll.del_element(3)
ll.del_value(6)

ll.pri()
