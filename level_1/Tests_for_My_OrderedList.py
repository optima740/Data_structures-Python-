import unittest
import My_OrderedList as mo

class TestMyStruct(unittest.TestCase):
    
    def test_add(self):
        ol = mo.OrderedList(True)
        ol.add(1)
        ol.add(3)
        ol.add(2)
        ol.add(0)
        my_list = ol.get_all()

        self.assertEqual(ol.head, my_list[0], 'incorrect self.head')
        self.assertEqual(ol.tail, my_list[3], 'incorrect self.tail')
        k=0
        for i in my_list:
            self.assertEqual(i.value, k, 'incorrect add for __ascending = True')
            k+=1
        self.assertEqual(ol.len(), 4, 'incorrect len')
        ol.clean(True)
        if ol.head != None or ol.tail != None or ol.len() != 0:
            print('incorrect clean')

        ol = mo.OrderedList(False)
        ol.add(2)
        ol.add(1)
        ol.add(3)
        ol.add(0)
        my_list = ol.get_all()
        k = 3
        for i in my_list:
            self.assertEqual(i.value, k, 'incorrect add for __ascending = False')
            k -= 1

test = TestMyStruct()
print(test.test_add())

