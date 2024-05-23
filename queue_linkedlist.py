#create queue using linked list

class Node:
    def __init__(self,value):
        self.info= value 
        self.next=None
class queue_linkedlist:
    def __init__(self):
      self.front=self.rear=None
    def addtoqueue(self,v): 
        n=Node(v)
        if self.rear==None:
            self.rear=self.front=n
        else:
            self.rear.next=n
            self.rear= n

    def deletefromqueue(self):
        if self.front==None:
            print("the queue is empty")
        else:
            self.front=self.front.next    
                

    def display(self):
        a=self.front
        while a:
            print(a.info,end="-->")
            a=a.next
        print("None")        


q=queue_linkedlist()
q.addtoqueue(23)
q.addtoqueue(34)
q.addtoqueue(45)
q.addtoqueue(60)
q.deletefromqueue()
q.display()  
