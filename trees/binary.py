from io import StringIO
import unittest
from unittest.mock import patch


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # inserting
    def insert(self, data):
        new_node = Node(data)
        # check root
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def delete(self, data):
        pass

    def isDataInTree(self, data):
        curr = self
        while curr.data != data:
            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right
            if curr is None:
                return False
        return True

    ''' BREADTH-FIRST TREE TRAVERSAL '''
    def PrintLevelOrder(self):
        queue = [self]
        while len(queue) > 0:
            curr = queue.pop(0)
            print(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    ''' DEPTH-FIRST TREE TRAVERSAL '''
    # print preorder <root><left><right>
    def PrintPreorder(self):
        print(self.data)
        if self.left:
            self.left.PrintPreorder()
        if self.right:
            self.right.PrintPreorder()

    # print inorder <left><root><right>
    def PrintInorder(self):
        if self.left:
            self.left.PrintInorder()
        print(self.data)
        if self.right:
            self.right.PrintInorder()

    # print postorder <left><right><root>
    def PrintPostorder(self):
        if self.left:
            self.left.PrintPreorder()
        if self.right:
            self.right.PrintPreorder()
        print(self.data)


# unit tests
class Test(unittest.TestCase):

    def test_print_preorder(self):
        root = Node(10)
        root.insert(6)
        root.insert(14)
        root.insert(3)
        root.insert(1)
        root.insert(4)
        root.insert(12)
        root.insert(18)
        root.insert(11)
        root.insert(7)

        print("Testing postorder...")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            root.PrintPreorder()
            self.assertEqual(fake_out.getvalue(), "10\n6\n3\n1\n4\n7\n14\n12\n11\n18\n")

    def test_print_inorder(self):
        root = Node(10)
        root.insert(6)
        root.insert(14)
        root.insert(3)
        root.insert(1)
        root.insert(4)

        print("Testing inorder...")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            root.PrintInorder()
            self.assertEqual(fake_out.getvalue(), "1\n3\n4\n6\n10\n14\n")

    def test_print_postorder(self):
        root = Node(10)
        root.insert(6)
        root.insert(14)
        root.insert(3)
        root.insert(1)
        root.insert(4)
        root.insert(12)
        root.insert(18)
        root.insert(11)
        root.insert(7)

        print("Testing postorder...")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            root.PrintPostorder()
            self.assertEqual(fake_out.getvalue(), "6\n3\n1\n4\n7\n14\n12\n11\n18\n10\n")

    def test_print_levelorder(self):
        root = Node(10)
        root.insert(6)
        root.insert(14)
        root.insert(3)
        root.insert(1)
        root.insert(4)

        print("Testing levelorder...")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            root.PrintLevelOrder()
            self.assertEqual(fake_out.getvalue(), "10\n6\n14\n3\n1\n4\n")

    def test_search(self):
        root = Node(10)
        root.insert(6)
        root.insert(14)
        root.insert(3)
        root.insert(1)
        root.insert(4)

        print("Testing isDataInTree...")
        self.assertTrue(root.isDataInTree(10))
        self.assertTrue(root.isDataInTree(1))
        self.assertFalse(root.isDataInTree(25))


if __name__ == '__main__':
    unittest.main()