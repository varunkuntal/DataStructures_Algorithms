class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = node()
        
        
    def append(self, data):
        new = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
            
        cur.next = new
        
        
    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count
        
    def display(self):
        cur = self.head
        ll = []
        while cur.next != None:
            cur = cur.next
            ll.append(cur.data)

        print(ll)
        
    def get(self, index):
        if index >= self.length():
            print("ERROR: Index greater than length")
            return None
        count = 0
        cur = self.head
        while True:
            cur = cur.next
            if count == index:
                return cur.data
            count += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: Index greater than length")
            return None
            
        count = 0
        cur = self.head
        while True:
            last = cur
            cur = cur.next
            if count == index:
                last.next = cur.next
                return
            count += 1
        
            
        
        
a = LL()  
a.append(3) 
a.append(-5)    
a.append(7)
a.append(12)
a.append(1) 
a.display()
a.erase(0)
a.display()
a.length()
print(a.get(1))
        
        
        
        
        
        
        
        
        
        
        
        
        
    