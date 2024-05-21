class Node:
    def __init__(self,value):
        self.info=value
        self.next=None
        self.prev=None

class  doubly_linkedlist:
    def __init__(self):   
        self.start=None
        #self.tail=None # for backward
    def insertatbeginning(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n
            # self.tail=n #for backward
        else:
            n.next=self.start
            self.start.prev=n
            self.start=n

    def insertatend(self,v):
        n=Node(v)
        if self.start==None:
            self.start=n 
        else:
            temp=self.start  
            while temp.next!=None:
                temp=temp.next
            temp.next=n
            n.prev=temp  

    def insertatmiddle(self,v,item):
        n=Node(v)
        if self.start==None:
            self.start=n
        else:
            temp=self.start
            while temp.info!=item:
                temp=temp.next
            n.next=temp.next   
            if temp.next:#check if temp.next is not none 
               temp.next.prev=n
            temp.next=n   
            n.prev=temp


    def display(self):
        a=self.start
        while a:
            print(a.info,end="-->")
            a=a.next
        print("None")


'''  def display2(self):
        a=self.tail
        while a:
            print(a.info)
            a=a.prev
        print("None")    '''#for backward print    

d=doubly_linkedlist()
d.insertatbeginning(20)
d.insertatbeginning(34)
d.insertatbeginning(67)
d.insertatend(40)
d.insertatmiddle(80,67)
d.display()  
# d.display2() for backward                      