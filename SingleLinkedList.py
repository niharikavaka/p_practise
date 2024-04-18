class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None 

    def append(self,data):
        new_node=Node(data)
        # print(new_node.data)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        
        while current_node.next is not None:
            current_node=current_node.next
        current_node.next=new_node  

          
            
         
    def display(self):
        if self.head is None:
            raise ValueError("No node exist")  
        current_node=self.head
        while current_node is not None:
            print(current_node.data,"--->",end=" ")
            current_node=current_node.next

    def insert_by_index(self,data,index):
        # new_node=Node(data)
        # count=0 
        # current_node=self.head
        # if self.head is None:
        #     self.head=new_node
        # while count == index:

        pass       
       
SLL=SingleLinkedList()
# SLL.append(10)
# SLL.append(20)
# SLL.append(30)
# SLL.append(40)
SLL.display()


