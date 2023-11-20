import unittest
import pokercombinations as Poker

class UnittestPoker(unittest.TestCase):


    def test_quads(self):
        hand=[[0,0,0,0,1],[0,0,0,0,1]]
        result= Poker.check_pairs(hand)
        self.assertEqual(result,"quads")

    def test_flush(self):
        hand=[[0,0,0,0,0],[1,4,5,4,9]]
        result=Poker.check_flush(hand,False)
        self.assertEqual(result,"flush")

    def test_pair(self):
        hand = [[0, 0, 0, 0, 1], [0, 0, 2, 2, 4]]
        result =Poker.check_pairs(hand)
        self.assertEqual("two-pair", result)



if __name__ == '__main__':
    unittest.main()