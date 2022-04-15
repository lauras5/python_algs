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

    # print inorder
    def PrintInorder(self):
        if self.left:
            self.left.PrintInorder()
        print(self.data)
        if self.right:
            self.right.PrintInorder()

    # print preorder
    def PrintPreorder(self):
        print(self.data)
        if self.left:
            self.left.PrintPreorder()
        if self.right:
            self.right.PrintPreorder()

    # print postorder
    def PrintPostorder(self):
        if self.left:
            self.left.PrintPreorder()
        if self.right:
            self.right.PrintPreorder()
        print(self.data)


# unit tests
class Test(unittest.TestCase):

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

    def test_print_preorder(self):
        root = Node(10)
        root.insert(6)
        root.insert(14)
        root.insert(3)
        root.insert(1)
        root.insert(4)

        print("Testing postorder...")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            root.PrintPreorder()
            self.assertEqual(fake_out.getvalue(), "10\n6\n3\n1\n4\n14\n")

    def test_print_postorder(self):
        root = Node(10)
        root.insert(6)
        root.insert(14)
        root.insert(3)
        root.insert(1)
        root.insert(4)

        print("Testing postorder...")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            root.PrintPostorder()
            self.assertEqual(fake_out.getvalue(), "6\n3\n1\n4\n14\n10\n")


if __name__ == '__main__':
    unittest.main()