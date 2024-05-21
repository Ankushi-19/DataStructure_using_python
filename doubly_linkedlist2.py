class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
        self.prev=None
class doubly_linkedlist:
    def __init__(self):     
        self.start=None

    def insertion(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
        else:
            n.next=self.start
            self.start.prev=n
            self.start=n

 # Delete from Beginning
    def deletefrombeginning(self):
        temp=self.start
        self.start=temp.next
        self.start.prev=None
        del temp
#Delete from Middle
    def deletefrommiddle(self,item):
        temp=self.start
        while temp.info!=item:
           prev=temp
           temp=temp.next  
        prev.next=temp.next
        temp.next.prev=prev 
        del temp

#Delete from End 
    def deletefromend(self):
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        temp.prev.next=None
        del temp




    def dispaly(self):
        a=self.start
        while a:
            print(a.info,end="--->")
            a=a.next 
        print("None")   


d=doubly_linkedlist()      
d.insertion(47)
d.insertion(90)
d.insertion(27)
d.insertion(12)
d.insertion(67)
d.insertion(100)   
d.deletefrombeginning()
d.deletefrommiddle(27) 
d.deletefromend()
d.dispaly()             
