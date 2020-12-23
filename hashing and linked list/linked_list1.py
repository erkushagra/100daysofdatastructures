class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data): #inserting data at the beginning of the linkedlist
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAfter(self,prev_node,new_data):#inserting data after the previous node(given)
        if prev_node ==None:
            print("The given previous node must in linkedlist")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self,new_data): #inserting data at last of the linkedlist
        new_node = Node(new_data)

        if self.head ==None:#if linkedlist is empty than make head as newnode
            self.head = new_node
            return self.head

        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp= temp.next

if __name__  == "__main__":
    Llist = Linkedlist()
    Llist.append(6)
    Llist.push(7)
    Llist.push(1)
    Llist.append(4)
    Llist.insertAfter(Llist.head.next,8)
    Llist.printlist()
    
    

        



        
        
