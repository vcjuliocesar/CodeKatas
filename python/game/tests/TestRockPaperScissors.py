import unittest

from ..src import RockPaperScissors

class TestRockPaperScissors(unittest.TestCase):
    
    #def test_when_user_and_pc_is_tie(self):
    
    def setUp(self):
        self.RockPaperScissors = RockPaperScissors
    
    def test_add(self):
        
        self.assertEqual( 2, self.RockPaperScissors.addition( 1 , 1) )
        
    