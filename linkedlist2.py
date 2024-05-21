class Node:
    def __init__(self,value):
       self.info=value
       self.next=None
class linkedlist:
    def __init__(self):
        self.start=None
    def insertatbeginning(self,v):    
        n=Node(v)
        if self.start==None:
            self.start=n
        else:
            n.next=self.start
            self.start=n

# Delete from beginning    
    def deletefrombeginning(self): 
        temp=self.start
        self.start=temp.next
        del temp

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
        while temp.next!=None:
            prev=temp
            temp=temp.next
        prev.next=None
        del temp


#Display
    def display(self):
        a=self.start
        while a:
           print(a.info,end="-->")
           a=a.next
        print("None")   


l=linkedlist()
l.insertatbeginning(36)
l.insertatbeginning(57)
l.insertatbeginning(34)
l.insertatbeginning(90)
l.insertatbeginning(89)
l.insertatbeginning(42)
l.insertatbeginning(12)
l.deletefrombeginning()
l.deletefrommiddle(57)
l.deletefromend()
l.display()
