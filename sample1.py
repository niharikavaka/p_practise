class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class SingleLinkedList:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def get_node_by_index(self, index):
        if not self.head:
            raise ValueError("No node exists")
        current_node = self.head
        count=0
        while count != index:
            current_node=current_node.next
            if not current_node:
                raise ValueError("Index out of range")
            count+=1
        print("Node at index -",index,"is ",current_node.data)
       
        if not self.head:
            raise ValueError("No node exists")
        current_node = self.head
        count=0
        previous_node = self.head
        while count != index:
            previous_node = current_node
            current_node=current_node.next
            if not current_node:
                raise ValueError("Index out of range")
            count+=1
        if previous_node:
            previous_node.next = current_node.next
            current_node.prev=previous_node
        elif not previous_node and current_node is not None:
             self.head = current_node.next
        else:
            self.head = None 
   
    def add_end(self,data):
        new_node=Node(data)
       
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n= n.next
            n.next=new_node  


    # add node middle 
    def add_after(self,data,x):
        n=self.head 
        while n is not None:
            if x==n.data:
                break 
            n=n.next
        if n is None:
            print("node is not present iin LL") 
        else:
            new_node=Node(data)
 
    def pop(self):
        if self.head is None:
            print("Empty List")

        current_node=self.head
        previous_node=self.head
        
        while current_node.next is not None:
            
                previous_node=current_node
                current_node=current_node.next
                 
        if previous_node == self.head == current_node:
            self.head = None     
        else:
             previous_node.next=None  

    def delete_by_value(self,x):
        if self.head is None:
            print("can't delete LL is empty!")
        if x==self.head.data:
            self.head=self.head.next
        n=self.head
        while n.next is not None:
            if x==n.next.data:
                break
            n=n.next
        if n.next is None:
            print("node is not present!")
        else:
            n.next=n.next.next

    def count(self):
        if not self.head:
            raise ValueError("No node exists")
        last_node = self.head
        count = 1
        while True:
            if last_node.next is None:
                break
            last_node = last_node.next
            count += 1
        return count        

                   
    # traversal
    def display(self):
        if self.head is None:
            print("linked list is empty")
        current_node = self.head
        while current_node is not None:
            print(current_node.data,"--->",end=" ") 
            
            current_node=current_node.next
        print(" ")    

    def add_node_by_index(self,index,data):
        new_node=Node(data)        
        if self.head is None:
            self.head=new_node
            return
        count = 0
        previous_node = None
        current_node = self.head
        while current_node.next is not None:
            if count == index:
                break
            previous_node = current_node
            current_node = current_node.next
            count += 1


        if current_node.next is None and count != index:
            current_node.next = new_node
           
        elif previous_node:
            previous_node.next = new_node
           
            new_node.next = current_node
           
        else:
            new_node.next = current_node
            self.head = new_node 
       

    def delete_node_by_index(self, index):
        if not self.head:
            raise ValueError("No node exists")
        previous_node = None 
        current_node = self.head
        count=0
        while count != index:
            if not current_node.next:
                raise ValueError("Index out of range")
            count+=1
            previous_node = current_node
            current_node = current_node.next
        if current_node == self.head:
            self.head = current_node.next
            
        else:
            previous_node.next = current_node.next

   
    def reverse(self):
       if self.head is None:
           print("empty list to reverse")
           return
       current_node=self.head
       previous_node=None
     
       while current_node is not None:
            k=current_node.next
            current_node.next=previous_node
            previous_node=current_node
            current_node=k
       self.head=previous_node     
          
   
    def clear(self):
        if self.head is None:
            print("It's already empty")
            return
        self.head=None
        print("cleared")   
    
    
    def sort(self):
        if not self.head or not self.head.next:
            print("ntg to sort")
            return
        current = self.head
        while current:
            runner = current.next
            while runner:
                if current.data > runner.data:
                    
                    
                    current.data, runner.data = runner.data, current.data
                runner = runner.next
            current = current.next
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def copy(self):
        copied_list = SingleLinkedList()
        current = self.head
        while current:
            copied_list.append(current.data)
            current = current.next
        return copied_list     
       

    def extend(self, other_list):
        if not other_list.head:
            return
        last_node_self = self.head
        while last_node_self.next:
            last_node_self = last_node_self.next
        last_node_self.next = other_list.head    
          
           
SLL=SingleLinkedList()
SLL.add_node_by_index(0,10)
SLL.add_node_by_index(1,40)
SLL.add_node_by_index(2,20)
SLL.add_node_by_index(3,30)   

copied_list = SLL.copy()
# copied_list.display()
linked_list2 = SingleLinkedList()
linked_list2.append(4)
linked_list2.append(5)
SLL.extend(linked_list2)
SLL.display()



             


         














































                












 


