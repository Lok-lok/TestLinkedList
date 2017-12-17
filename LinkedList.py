'''
Created on Dec,16th,2017

@author: Lok
'''

class Node():
    
        def __init__(self, data):
            if isinstance(data,int):
                self.data=data
                self.previous=None
                self.next=None
            elif data==None:
                self.data=None
                self.previous=None
                self.next=None
            else:
                raise TypeError("input must be an int")
        
        def __str__(self):
            return self.data

class LinkedList():       
    def __init__(self):
        self.first=Node(None)
        self.last=Node(None)
        self.first.next=self.last
        self.last.previous=self.first
        self.size=0
        
    def __str__(self):
        s="("
        current=self.first.next
        for i in range(0,self.size):
            s=s+str(current.data)+" "
            current=current.next
        s=s+")"
        return s
        
    def addToFront(self,data):
        if isinstance(data, int):
            p=self.first.next
            newAdded=Node(data)
            
            p.previous=newAdded
            newAdded.next=p
            newAdded.previous=self.first
            self.first.next=newAdded
            self.size+=1
        else:
            raise TypeError("input must be an int")   
    
    def addToBack(self, data):
        if isinstance(data, int):
            p=self.last.previous
            newAdded=Node(data)
            
            p.next=newAdded
            newAdded.previous=p
            newAdded.next=self.last
            self.last.previous=newAdded
            self.size+=1
        else:
            raise TypeError("input must be an int")
    
    
    def removeFront(self):
        '''
            return an int
        '''
        n=self.first.next
        self.first.next=n.next
        n.next.previous=self.first
        self.size-=1
        return n.data
    
    def removeLast(self):
        '''
            return an int
        '''
        n=self.last.previous
        self.last.previous=n.previous
        n.previous.next=self.last
        self.size-=1
        return n.data
    
    def size(self):
        return self.size
    
    def front(self):
        return self.first.next.data
    
    def get(self,pos):
        '''
            return an int.
        '''
        if not isinstance(pos, int):
            raise TypeError("position must be an int")
        if not pos>=0&pos<self.size:
            raise TypeError("position out of range")
        
        current=self.first
        for i in range(0,pos):
            current=current.next
        return current.data
    
    def insert(self,data,pos):
        if not isinstance(data, int):
            raise TypeError("input must be an int")
        if not isinstance(pos, int):
            raise TypeError("position must be an int")
        if not pos>=0&pos<self.size:
            raise TypeError("position out of range")
        
        current=self.first
        for i in range(0,pos):
            current=current.next
        p=current.previous
        newAdded=Node(data)
        p.next=newAdded
        newAdded.previous=p
        newAdded.next=current
        current.previous=newAdded
        self.size+=1
        
    def remove(self,pos):
        '''
            return an int.
        '''
        if not isinstance(pos, int):
            raise TypeError("position must be an int")
        if not pos>=0&pos<self.size:
            raise TypeError("position out of range")
        
        current=self.first
        for i in range(0,pos):
            current=current.next
        current.previous.next=current.next
        current.next.previous=current.previous
        self.size-=1
        return current.data
        
    def contains(self,data):
        '''
            return the number of the given elements contained in the LinkedList.
        '''
        contains=0
        current=self.first
        for i in range(0,self.size):
            if current.data==data:
                contains+=1
            current=current.next
        return contains
        
if __name__=="__main__":
    LinkedList=LinkedList()
    LinkedList.addToBack(5)
    LinkedList.addToFront(10)
    LinkedList.addToBack(12)
    LinkedList.insert(7, 1)
    LinkedList.insert(6, 1)
    print(LinkedList.get(2))
    print(LinkedList.remove(2))
    print(LinkedList)
    print(LinkedList.size)
    print(LinkedList.contains(10))
    print(LinkedList.removeFront());
    print(LinkedList.removeFront());
    print(LinkedList.removeLast());
    print(LinkedList.size)
    