class Node:
    # create a node
    def __init__(self, data, next=None):
        # node has two parts data and referance of next node to which it is poinitng
        self.data = data
        self.next = next
        # by default the next value is None
        # mans new node point to none or nothing


class LinkList:
    # this is to insert element in node.
    # insertion at begning of node, at end, inbetween two nodes
    def __init__(self):
        self.head = None
        # here we are creating empty linked list as when head point to none that measn list is empty there is no node.
        # as head has the reference of first node

    def create_element(self, data):
        # here we are creating a node which will have data and referecne of next node
        node = Node(data, self.head)
        self.head = node

        # here now head poit to object we created or node created.
        # self.head contain the reference

    def print_list(self):
        if self.head == None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                # to traverse the linked list.means until node contain no refernce of next node that means we are atend or no element is there. as n=self.head intinally as self.head = None that means no eleemnt is there.
                print(f"data : {n.data}")
                n = n.next
                # this is n = self.head.next
                # now again when wile loop execute n=n.next self.head.next.next that mean it contain reference of third element.


ll = LinkList()
ll.create_element(12)
