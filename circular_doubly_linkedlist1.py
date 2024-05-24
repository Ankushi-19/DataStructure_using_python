class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
        self.prev=None

class circular_doublylinkedlist:
    def __init__(self):
        self.start=None

    def insertatbeginning(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=n
            self.start.prev=n
        else:
            n.next=self.start
            temp=self.start  
            temp.prev=n
            while temp.next!=self.start:
                temp=temp.next
            self.start=n    
            temp.next=n    
            n.prev=temp
    def insertatmiddle(self,v,item):
        n=Node(v)
        if self.start==None: 
           self.start=n
           self.start.next=n 
           self.start.prev=n  
        else:  
            temp=self.start
            while temp.info!=item:
                temp=temp.next
            n.next=temp.next
            temp.next.prev=n        
            temp.next=n
            n.prev=temp

    def insertatend(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=self.start.prev=n
        else:
            temp=self.start
            while temp.next!=self.start:
                temp=temp.next
            temp.next=n
            n.prev=temp
            n.next=self.start
            self.start.prev=n 
              


    def display(self):
        if self.start==None:
            print("the list is empty")
            return
        a=self.start
        while a:
            print(a.info,end="-->")
            a=a.next
            if a==self.start:
                break
        print("start")   


d=circular_doublylinkedlist()
d.insertatbeginning(78)
d.insertatbeginning(90)
d.insertatbeginning(56) 
d.insertatmiddle(12,90)
d.insertatend(33)
d.display()              

