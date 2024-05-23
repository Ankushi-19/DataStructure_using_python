class Node:
    def __init__(self,value):
        self.info=value
        self.next=None

class circular_linkedlist:
    def __init__(self):
        self.start=None

    def insertion(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            self.start.next=n
        else:
            n.next=self.start
            temp=self.start
            while temp.next!=self.start:
                temp=temp.next
            temp.next=n
            self.start=n   

#Delete from Beginning
    def deletefrombeginning(self):
            temp=self.start
            while temp.next!=self.start:
                temp=temp.next
            self.start=self.start.next 
            temp.next=self.start  
             
#Delete from Middle
    def deletefrommiddle(self,item):
        temp=self.start
        while temp.info!=item:
            prev=temp
            temp=temp.next
        prev.next=temp.next
        del temp  

#Delete from End
    def deletefromend(self):
        temp=self.start
        while temp.next!=self.start:
            prev=temp
            temp=temp.next
        prev.next=self.start
        del temp    



    def display(self):
        if  self.start==None:
            print("list is empty")
            return
        a=self.start
        while a:
            print(a.info,end="-->")
            a=a.next
            if a==self.start:
                break
        print("start")





c=circular_linkedlist()
c.insertion(33)
c.insertion(22)
c.insertion(55)  
c.insertion(78)
c.insertion(12)
c.insertion(900)
c.deletefrombeginning()
c.deletefrommiddle(55)
c.deletefromend()
c.display()           


