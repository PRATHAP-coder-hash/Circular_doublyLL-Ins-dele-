class node:
    def __init__(self,data):
        self.data = data
        self.nxt = None
        self.prev = None
class cdll:
    def __init__(self):
        self.head = None
        self.tail = None
    def create(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.nxt = self.head
            self.tail.nxt = self.head
        else:
            self.tail.nxt = new_node
            self.head.prev = new_node
            new_node.nxt = self.head
            new_node.prev = self.tail
            self.tail = new_node
    def insert(self,pos,data):
        new_node = node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.nxt = self.head
            self.head.prev = self.head
        if pos == 1:
            new_node.nxt = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.nxt = new_node
            self.head = new_node
        else:
            temp = self.head
            for i in range(1,pos-1):
                temp = temp.nxt
            new_node.nxt = temp.nxt
            new_node.prev = temp
            temp.nxt.prev = new_node
            temp.nxt = new_node
    def delete(self,pos):
        if self.head is None:
            print("List is empty")
        if pos == 1:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.nxt
                self.head.prev = self.tail
                self.tail.nxt = self.head
        else:
            temp = self.head
            for i in range(1,pos):
                temp = temp.nxt
            if temp == self.tail:
                self.tail = self.tail.prev
                self.tail.nxt = self.head
                self.head.prev = self.tail
                temp.nxt = None
                temp.prev = None
            else:
                temp.prev.nxt = temp.nxt
                temp.nxt.prev = temp.prev
                temp.nxt = None
                temp.prev = None
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while True:
                print(current.data,end="-->")
                current = current.nxt
                if current == self.head:
                    break
            print("Head")
            current = self.tail
            while True:
                print(current.data,end="<--")
                current = current.prev
                if current == self.tail:
                    break
            print("Tail")
def main():
    l = cdll()
    while True:
        print("1.Create Circular Doubly LL:")
        print("2.Insert")
        print("3.Delete")
        print("4.Display")
        print("5.Exit")
        opt = input("Select an option:")
        if opt == "1":
            n = int(input("Enter no.of node:"))
            for i in range(n):
                data = input(f'enter data for node {i+1}:')
                l.create(data)
        elif opt == "2":
            pos = int(input("Enter position to insert:"))
            data = input("Enter data to insert:")
            l.insert(pos,data)
        elif opt == "3":
            pos = int(input("Enter position to delete:"))
            l.delete(pos)
        elif opt == "4":
            l.display()
        elif opt == "5":
            break
        else:
            print("Invalid!, Try again:")
if __name__ == "__main__":
    main()