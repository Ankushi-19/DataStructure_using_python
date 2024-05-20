class Node:
 def __init__(self,value):
    self.info=value
    self.next=None

class linkedlist:
  def __init__(self):
    self.start=None

#Insert at Beginning    
  def insertatbegining(self,v):
    n=Node(v)
    if self.start==None:
        self.start=n
    else:
       n.next=self.start
       self.start=n 

#Insert at middle
  def insertatmiddle(self,v,item):
    n=Node(v)
    if self.start==None:
      self.start=n
    else: 
      temp=self.start
      while temp.info!=item:
        temp=temp.next
      n.next=temp.next 
      temp.next=n 

#Insert at End
  def insertatend(self,v):
    n=Node(v)
    if self.start==None:
      self.start=n
    else:
      temp=self.start
      while temp.next!=None:
        temp=temp.next
      temp.next=n
        
#Display
  def display(self):
    a=self.start
    while a:
      print(a.info,end="-->")
      a=a.next
    print("None")  


l=linkedlist()
l.insertatbegining(63)
l.insertatbegining(89)
l.insertatbegining(99) 
l.insertatbegining(56)   
l.insertatmiddle(16,99)
l.insertatend(30)
l.display()


