class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
        self.prev=None

class    circular_doublylinkedlist:
    def __init__(self):
        self.start=None

    def insertion(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=self.start.prev=n
        else:
            n.next=self.start
            temp=self.start
            temp.prev=n
            while temp.next!=self.start:
                temp=temp.next
            temp.next=n               
            n.prev=temp
            self.start=n

#Delete from beginning
    def deletrfrombeginning(self):
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        self.start=self.start.next
        temp.next=self.start
        self.start.prev=temp
        del temp

#Delete from middle
    def deletefrommiddle(self,item):
        temp=self.start
        while temp.info!=item:
            prev=temp
            temp=temp.next
        prev.next=temp.next 
        temp.next.prev=prev
        del temp   

#Delete from end
    def deletefromend(self):
        temp=self.start
        while temp.next!=self.start:
            prev=temp
            temp=temp.next 
        prev.next=self.start
        self.start.prev=prev
        del temp            
                 


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

c=circular_doublylinkedlist()
c.insertion(56)
c.insertion(12)
c.insertion(70)
c.insertion(22)
c.insertion(33)
c.insertion(10)
c.deletrfrombeginning()
c.deletefrommiddle(70)
c.deletefromend()
c.display()                 