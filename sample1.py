# # # # #string_compression
# # # # a="aaabbccd"
# # # # b=''
# # # # count=1
# # # # for i in range(len(a)-1):
# # # #     if a[i] == a[i+1]:
# # # #         count+=1
# # # #     else:
# # # #         b=b+a[i]+str(count)
# # # #         count=1
# # # # b=b+a[i+1]+str(count)        

# # # # print(b)

# # # # import json
# # # # a=open("dmy_1.json",'w')


# # # # k=json.dump([1,2,3,4],a)

# # # # a.close()
# # # # k=json.dump([5],open("dmy_1.json","a"))

# # # # # import json 
# # # # # x=[1,2,3,4,5]
# # # # # json.dump(x,open('dmy_1.py',"r+"))
# # # # # n=json.load(open('dmy_1.py'))
# # # # # print(type(n))
# # # # # y=json.dumps(x)
# # # # # print(type(y))
# # # # # z=json.loads(y)
# # # # # print(type(z))
# # # def add(a,b):
# # #     print(a+b)
# # # add(2,3)    

# # # import argparse 
# # # parser=argparse.ArgumentParser(description="description...")
# # # parser.add_argument('sample.py',help="adding two values")

# # # args = parser.parse_args()
# # # print(args.filename)

# # class Node:
# #     def  __init__(self,data):
# #         self.data=data
# #         self.next=None

# # class SLL:
# #     def __init__(self):
# #         self.head=None 

# #     def append(self,data):
# #         new_node=Node(data)
# #         if self.head is None:
# #             self.head = new_node 
# #         else:
# #             current = self.head 
# #             while current.next is not None:
# #                 current=current.next
# #             current.next=new_node 
# #     def display(self):
# #         if self.head is None:
# #             print("Linked list is empty!")
# #         else:
# #             n=self.head 
# #             while n is not None:
# #                 print(n.data)
# #                 n=n.next


# # k=SLL()
# # k.append(10)
# # k.append(20)
# # k.display()


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None 
#         self.next=None 
# class DoubleLinkedList:
#     def __init__(self):
#         self.head=None 

#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             n=self.head
#             while n.next is not None:
#                 n=n.next 
#             n.next=new_node
#             new_node.prev=n   

#     def get_node(self,index):
#         count=0
#         current_node=self.head
       
#         if current_node is None:
#             print("No Node Exist")
#         else:    
#             while count != index:
#                 current_node=current_node.next
#                 if not current_node:
#                   raise ValueError("Index out of range")
#                 # current_node=current_node.next 
#                 count+=1
                     
#             print(current_node.data)
      
       








#     def display(self):
#         if self.head is None:
#             print("Its empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data)
#                 n=n.next
#     def delete_by_index(self,index):
#          count=0
#          current_node=self.head
#          while count != index:
#                 current_node=current_node.next 
#                 count+=1
       
#          current_node.prev.next=current_node.next
#          current_node.next.prev=current_node.prev
#         #  current_node.next.prev=k
#         #  n=current_node.next.prev
#         #  current_node.prev=n 
       
#         #  del current_node

         





# DLL=DoubleLinkedList()
# DLL.append(10)
# DLL.append(20)
# DLL.append(130)
# DLL.append(140)
# DLL.get_node(4)
# # DLL.delete_by_index(1)
# DLL.display()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class SingleLinkedList:
    def __init__(self):
        self.head=None


       


   
    # adding at beginning 
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
        # return current_node.data
    
    # def delete1_node_by_index(self, index):
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
    #adding at end
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
            

        
   


      



      

      
        

       
        
    def add_node(self,index,data):
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
            # print(k.data)
           
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
    
   
   
        
    # def sort(self):
      
    #     if self.head is None:
    #         print("EMpty list to sort")
    #         return

    #     result=[]
    #     current_node=self.head
    #     while  current_node is not None:
    #         # print(current_node.data)
    #         result.append(current_node.data)
    #         current_node=current_node.next
         
    #     # print(self.head.data)
    #     result.sort()  
    #     self.head=None  
    #     for i in range(len(result)):
           
    #        self.add_node(0,result[i])
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
    

    # def copy(self):
       
    #     new_linked_list = SingleLinkedList()

       
    #     current = self.head
    #     while current:
    #         new_linked_list.add_end(current.data)
    #         current = current.next


       
          
           




             


         







SLL=SingleLinkedList()

# SLL.delete_by_value(20)


# SLL.add_node(0,10)

# SLL.add_node(1,40)
# SLL.add_node(2,20)
# SLL.add_node(3,30)

# SLL.clear()
# SLL.get_node_by_index(6)

SLL.sort()
# SLL.reverse()
SLL.display()




















# SLL.display()







                












 


