class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList():
    def __init__(self):
        self.head=Node("Fuck")
        self.Start=self.head

    def printlist(self):
        while self.head.next != None:
            print(self.head.data)
            self.head=self.head.next
        print(self.head.data)
        self.head = self.Start

    def insert_begin(self,Node):
        Node.next=self.Start
        self.head=Node
        self.Start=self.head

    def insert_last(self,Node):
        while self.head.next!=None:
            self.head=self.head.next
        self.head.next=Node
        self.head = self.Start






if __name__ =="__main__":
    h1=SinglyLinkedList()
    h2=Node("U")
    h3=Node("Son of a Bitch")

    #Add Nodes to list
    h1.head.next=h2
    h2.next=h3
    #h1.printlist()

    # Insert at Beginning
    h4=Node("_|_")
    h1.insert_begin(h4)
    #h1.printlist()

    # Insert at last
    h5=Node("MotherFucker")
    h1.insert_last(h5)
    h1.printlist()



