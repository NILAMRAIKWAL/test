from flask import Flask

app = Flask(__name__)

@app.route('/')
class Node:
    def __inti__(self,val):
        self.left = None
        self.right = None
        self.value = val

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
            if self.right:
                return self.right.find(data)
            else:
                return False


    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))

class Tree:
    def __inti__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False


    def postorder(self):
        print("PostOrder")
        self.root.postorder()



bst = Tree()
print (bst.insert(10))
bst.insert(14)
bst.postorder()


if __name__== "__main__":
    app.run()