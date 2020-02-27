import unittest

import My_SimpleTree as tr
class My_Tests(unittest.TestCase):

    def test_add(self):
        node1 = tr.SimpleTreeNode('1', None)
        node2 = tr.SimpleTreeNode('1.1', None)
        node3 = tr.SimpleTreeNode('1.2', None)
        node4 = tr.SimpleTreeNode('1.2.1', None)
        node5 = tr.SimpleTreeNode('1.2.2', None)

        My_tree = tr.SimpleTree(node1)
        self.assertEqual(My_tree.Root, node1, 'incorrect add Root')
        self.assertEqual(node1.Parent, None, 'incorrect Root parent reference')
        My_tree.AddChild(node1, node2)
        My_tree.AddChild(node1, node3)
        self.assertEqual(len(node1.Children), 2, 'incorrect Root number children')
        self.assertEqual(node1.Children[0], node2, 'incorrect Root reference 0 children')
        self.assertEqual(node1.Children[1], node3, 'incorrect Root reference 1 children')
        self.assertEqual(node1.Children[0].Parent, node1, 'incorrect child0 reference 0 parent')
        self.assertEqual(node1.Children[1].Parent, node1, 'incorrect child1 reference 1 parent')
        self.assertEqual(len(node1.Children[0].Children), 0, 'incorrect number children for children0')
        self.assertEqual(len(node1.Children[1].Children), 0, 'incorrect number children for children1')

        My_tree.AddChild(node3, node4)
        My_tree.AddChild(node3, node5)

        self.assertEqual(len(node1.Children[1].Children), 2, 'incorrect number children for children1 after add')
    def test_count(self):
        node1 = tr.SimpleTreeNode('1', None)
        node2 = tr.SimpleTreeNode('1.1', None)
        node3 = tr.SimpleTreeNode('1.2', None)
        node4 = tr.SimpleTreeNode('1.2.1', None)
        node5 = tr.SimpleTreeNode('1.2.2', None)
        node6 = tr.SimpleTreeNode('1.2.1.1', None)

        My_tree = tr.SimpleTree(node1)
        self.assertEqual(My_tree.Count, 1, 'incorrect count root')
        My_tree.AddChild(node1, node2)
        My_tree.AddChild(node1, node3)
        My_tree.AddChild(node3, node4)
        My_tree.AddChild(node3, node5)
        My_tree.AddChild(node4, node6)
        self.assertEqual(My_tree.Count(), 6, 'incorrect count nodes')

    def test_remove(self):
        node1 = tr.SimpleTreeNode('1', None)
        node2 = tr.SimpleTreeNode('1.1', None)
        node3 = tr.SimpleTreeNode('1.2', None)
        node4 = tr.SimpleTreeNode('1.2.1', None)
        node5 = tr.SimpleTreeNode('1.2.2', None)
        node6 = tr.SimpleTreeNode('1.2.1.1', None)
        My_tree = tr.SimpleTree(node1)
        My_tree.AddChild(node1, node2)
        My_tree.AddChild(node1, node3)
        My_tree.AddChild(node3, node4)
        My_tree.AddChild(node3, node5)
        My_tree.AddChild(node4, node6)
        My_tree.DeleteNode(node6)
        self.assertEqual(len(node4.Children), 0, 'incorrect len children parent node')
        self.assertEqual(My_tree.Count(), 5, 'incorrect count nodes')
        self.assertEqual(node6.Parent, None, 'incorrect reference parent node6')
        My_tree.DeleteNode(node3)
        self.assertEqual(My_tree.Count(), 2, 'incorrect count nodes')
        My_tree.DeleteNode(node1)
        self.assertEqual(My_tree.Count(), 0, 'incorrect count nodes')
        self.assertEqual(My_tree.Root, None, 'incorrect Root reference')

    def test_get_all_nodes(self):
        node1 = tr.SimpleTreeNode('1', None)
        node2 = tr.SimpleTreeNode('1.1', None)
        node3 = tr.SimpleTreeNode('1.2', None)
        node4 = tr.SimpleTreeNode('1.2.1', None)
        node5 = tr.SimpleTreeNode('1.2.2', None)
        node6 = tr.SimpleTreeNode('1.2.1.1', None)
        My_tree = tr.SimpleTree(node1)
        My_tree.AddChild(node1, node2)
        My_tree.AddChild(node1, node3)
        My_tree.AddChild(node3, node4)
        My_tree.AddChild(node3, node5)
        My_tree.AddChild(node4, node6)

        test_list = [node1, node2, node3, node4, node5, node6]
        current_list = My_tree.GetAllNodes()

        count = 0
        for node in test_list:
            flg = 0
            for item in current_list:
                if node == item:
                    flg = 1
                    count += 1
            self.assertEqual(flg, 1, 'incorrect current list')
        self.assertEqual(count, 6, 'incorrect size current list')
        self.assertEqual(len(current_list), 6, 'incorrect len current list')

    def test_move_node(self):
        node1 = tr.SimpleTreeNode('1', None)
        node2 = tr.SimpleTreeNode('1.1', None)
        node3 = tr.SimpleTreeNode('1.2', None)
        node4 = tr.SimpleTreeNode('1.2.1', None)
        node5 = tr.SimpleTreeNode('1.2.2', None)
        node6 = tr.SimpleTreeNode('1.2.1.1', None)
        My_tree = tr.SimpleTree(node1)
        My_tree.AddChild(node1, node2)
        My_tree.AddChild(node1, node3)
        My_tree.AddChild(node3, node4)
        My_tree.AddChild(node3, node5)
        My_tree.AddChild(node4, node6)
        node_find = My_tree.FindNodesByValue('1.2')
        node_find1 = My_tree.FindNodesByValue('1.1')
        self.assertEqual(len(node2.Children), 0, 'incorrect reference child nodes2')
        My_tree.MoveNode(node_find[0], node_find1[0])
        self.assertEqual(My_tree.Count(), 6, 'incorrect count nodes, after move')
        self.assertEqual(len(node1.Children), 1, 'incorrect reference child nodes, after move')
        self.assertEqual(node3.Parent, node2, 'incorrect reference parent, after move')
        self.assertEqual(node2.Children[0], node3, 'incorrect reference child[0], after move')

test = My_Tests()
test.test_add()
test.test_count()
test.test_remove()
test.test_get_all_nodes()
test.test_move_node()