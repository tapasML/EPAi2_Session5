import pytest
import random
import string
import math
import session_5_assignment
from session_5_assignment import *


# testcase #1
def test_Poker():
    
    ##################
    # 5 card hands ###
    ##################
    
    # 5 card RoyalFlush Tie
    player1=[('A', 'spades'),  ('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]
    player2=[('A', 'clubs'),  ('10', 'clubs'), ('K', 'clubs'), ('Q', 'clubs'), ('J', 'clubs')]
    assert playpoker(player1, player2) == 'Tie', 'should have been a tie!'
    
    # 5 card RoyalFlush vs StraightFlush
    player1=[('A', 'spades'),  ('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]
    player2=[('9', 'clubs'),  ('10', 'clubs'), ('K', 'clubs'), ('Q', 'clubs'), ('J', 'clubs')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    # 5 card RoyalFlush vs Flush
    player1=[('A', 'spades'),  ('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]
    player2=[('9', 'clubs'),  ('2', 'clubs'), ('6', 'clubs'), ('Q', 'clubs'), ('3', 'clubs')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    # 5 card Straight:win using tiebreaker
    player1=[('7', 'spades'),  ('4', 'diamonds'), ('3', 'clubs'), ('2', 'hearts'), ('5', 'spades')]
    player2=[('7', 'diamonds'),  ('4', 'spades'), ('3', 'hearts'), ('5', 'clubs'), ('6', 'diamonds')]
    assert playpoker(player1, player2) == 'player2', 'player2 should win!'
    
    # 5 card HighCard 
    player1=[('10', 'spades'),  ('8', 'diamonds'), ('6', 'clubs'), ('4', 'hearts'), ('2', 'spades')]
    player2=[('K', 'diamonds'),  ('J', 'spades'), ('7', 'hearts'), ('5', 'clubs'), ('2', 'diamonds')]
    assert playpoker(player1, player2) == 'player2', 'player2 should win!'
    
    # 5 card Straight vs ThreeOfaKind
    player1=[('9', 'spades'),  ('9', 'diamonds'), ('9', 'clubs'), ('2', 'hearts'), ('A', 'spades')]
    player2=[('7', 'diamonds'),  ('4', 'spades'), ('3', 'hearts'), ('5', 'clubs'), ('6', 'diamonds')]
    assert playpoker(player1, player2) == 'player2', 'player2 should win!'
    
    # 5 card FourOfaKind vs FullHouse
    player1=[('9', 'spades'),  ('9', 'diamonds'), ('9', 'clubs'), ('9', 'hearts'), ('A', 'spades')]
    player2=[('K', 'diamonds'),  ('K', 'spades'), ('K', 'hearts'), ('2', 'clubs'), ('2', 'diamonds')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
     # 5 card HighCard 
    player1=[('10', 'spades'),  ('8', 'diamonds'), ('6', 'clubs'), ('4', 'hearts'), ('2', 'spades')]
    player2=[('K', 'diamonds'),  ('J', 'spades'), ('7', 'hearts'), ('5', 'clubs'), ('2', 'diamonds')]
    assert playpoker(player1, player2) == 'player2', 'player2 should win!'
    
    ############
    # 4 card ###
    ############
    
    # 4 card StraightFlush vs FourOfaKind
    player1=[('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]
    player2=[('5', 'clubs'), ('5', 'hearts'), ('5', 'spades'), ('5', 'diamonds')]
    assert playpoker(player1, player2) == 'player2', 'player2 should win!'
    
    
    # 4 card Flush vs Straight
    player1=[ ('3', 'spades'), ('5', 'spades'), ('7', 'spades'), ('9', 'spades')]
    player2=[('9', 'clubs'),  ('10', 'diamonds'), ('J', 'spades'), ('Q', 'clubs')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    
    # 4 card OnePair vs HighCard
    player1=[ ('3', 'spades'), ('3', 'clubs'), ('7', 'hearts'), ('9', 'diamonds')]
    player2=[('9', 'clubs'),  ('5', 'diamonds'), ('2', 'hearts'), ('Q', 'clubs')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    # 4 card Flush vs TwoPairs
    player1=[ ('3', 'spades'), ('5', 'spades'), ('7', 'spades'), ('9', 'spades')]
    player2=[('9', 'clubs'),  ('9', 'diamonds'), ('2', 'hearts'), ('2', 'clubs')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    
    # 4 card Straight vs Straight Tiebreaker
    player1=[('3', 'spades'), ('6', 'hearts'), ('5', 'clubs'), ('4', 'diamonds')]
    player2=[('7', 'spades'), ('8', 'hearts'), ('9', 'clubs'), ('10', 'diamonds')]
    assert playpoker(player1, player2) == 'player2', 'player1 should win!'
    
    
    # 4 card HighCard vs HighCard TieBreaker
    player1=[('3', 'spades'), ('7', 'hearts'), ('Q', 'clubs'), ('A', 'diamonds')]
    player2=[('2', 'spades'), ('5', 'hearts'), ('3', 'clubs'), ('10', 'diamonds')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    # 4 card ThreeOfaKind vs Flush 
    player1=[('3', 'spades'), ('3', 'hearts'), ('3', 'clubs'), ('2', 'diamonds')]
    player2=[('A', 'spades'), ('5', 'spades'), ('4', 'spades'), ('10', 'spades')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    ############
    # 3 card ###
    ############
   
    # 3 card Flush vs Straight
    player1=[ ('3', 'spades'), ('7', 'spades'), ('9', 'spades')]
    player2=[('9', 'clubs'),  ('10', 'diamonds'), ('J', 'spades')]
    assert playpoker(player1, player2) == 'player2', 'player2 should win!'
    
    # 3 card ThreeOfaKind vs Flush 
    player1=[('3', 'spades'), ('3', 'hearts'), ('3', 'clubs')]
    player2=[('A', 'spades'), ('Q', 'spades'), ('10', 'spades')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    # 3 card OnePair vs HighCard 
    player1=[('3', 'spades'), ('3', 'hearts'), ('6', 'clubs')]
    player2=[('A', 'spades'), ('Q', 'hearts'), ('10', 'diamonds')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    
    # 3 card Straight vs Straight Tiebreaker
    player1=[('3', 'spades'), ('5', 'clubs'), ('4', 'diamonds')]
    player2=[('7', 'spades'), ('9', 'clubs'), ('10', 'diamonds')]
    assert playpoker(player1, player2) == 'player1', 'player1 should win!'
    
    
    # 3 card Flush vs Flush TieBreaker
    player1=[('3', 'spades'), ('7', 'spades'), ('9', 'spades')]
    player2=[('4', 'clubs'), ('8', 'clubs'), ('9', 'clubs')]
    assert playpoker(player1, player2) == 'player2', 'player2 should win!'
    
    
# testcase #2
def test_DuplicateCard():
    player1=[('3', 'spades'), ('7', 'spades'), ('9', 'spades')]
    player2=[('3', 'spades'), ('8', 'clubs'), ('9', 'clubs')]
    with pytest.raises(ValueError):   
        assert playpoker(player1, player2) == ValueError

# testcase #3
def test_DiffernetNoOfCards():
    player1=[('3', 'spades'), ('7', 'spades'), ('9', 'spades')]
    player2=[('3', 'spades'), ('8', 'clubs'), ('9', 'clubs'), ('J', 'clubs')]
    with pytest.raises(ValueError):   
        assert playpoker(player1, player2) == ValueError

# testcase #4        
def test_6_Cards():
    player1=[('3', 'spades'), ('3', 'hearts'), ('3', 'clubs'), ('2', 'diamonds'), ('K', 'hearts'), ('Q', 'hearts')]
    player2=[('A', 'spades'), ('5', 'spades'), ('4', 'spades'), ('10', 'spades'), ('K', 'spades'), ('Q', 'clubs')]
    with pytest.raises(ValueError):   
        assert playpoker(player1, player2) == ValueError
        

# testcase #5
def test_createdeck_reg():
    assert len(createdeck_reg()) == 52
    

# testcase #6
def createdeck_lambda():
    assert len(createdeck_lambda()) == 52
    

# testcase #7    
def test_isSequence():
    player1=[('3', 'spades'), ('4', 'spades'), ('2', 'spades')]
    #assert _isSequence(player1), 'Should be a sequence'
    isSequence(player1)

# testcase #8    
def test_isSequence_Negative():
    player1=[('6', 'spades'), ('4', 'spades'), ('2', 'spades')]
    assert isSequence(player1) == False, 'Should not be a sequence'
    
# testcase #9    
def test_isSameSuite():
    player1=[('6', 'spades'), ('4', 'spades'), ('2', 'spades')]
    assert isSameSuite(player1) , 'Should be same suite'
    
# testcase #10
def testisRoyalFlush():
    player1=[('A', 'spades'),  ('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]
    assert isRoyalFlush(player1) , 'Should be RoyalFlush'
    
# testcase #11
def test_isStraightFlush():
    player1=[('9', 'spades'),  ('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]
    assert isStraightFlush(player1) , 'Should be StrightFlush'
    
# testcase #12
def test_isFourOfaKind():
    player1=[('10', 'spades'),  ('J', 'spades'), ('10', 'hearts'), ('10', 'clubs'), ('10', 'diamonds')]
    assert isFourOfaKind(player1) , 'Should be FourOfaKind'
    

# testcase #13  
def test_isFullHouse():
    player1=[('10', 'spades'),  ('J', 'hearts'), ('J', 'spades'), ('10', 'clubs'), ('10', 'diamonds')]
    assert isFullHouse(player1) , 'Should be FullHouse'  


# testcase #14    
def test_isFlush():
    player1=[('10', 'hearts'),  ('J', 'hearts'), ('4', 'hearts'), ('6', 'hearts')]
    assert isFlush(player1) , 'Should be Flush' 
    
# testcase #15    
def test_isStraight():
    player1=[('10', 'spades'),  ('J', 'hearts'), ('9', 'clubs')]
    assert isStraight(player1), 'Should be Straight' 
    
# testcase #16  
def test_isThreeOfaKind():
    player1=[('6', 'spades'),  ('5', 'spades'), ('6', 'clubs'), ('6', 'diamonds'), ('4', 'hearts')]
    assert isThreeOfaKind(player1) , 'Should be ThreeOfaKind' 
    

# testcase #16  
def test_isThreeOfaKind_Negative():
    player1=[('6', 'spades'),  ('5', 'spades'), ('6', 'clubs'), ('6', 'diamonds'), ('5', 'hearts')]
    assert not isThreeOfaKind(player1) , 'Should not be ThreeOfaKind, it is a FullHouse!' 


# testcase #17
def test_isThreeOfaKind_Negative():
    player1=[('6', 'spades'),  ('5', 'spades'), ('6', 'clubs'), ('6', 'diamonds'), ('5', 'hearts')]
    assert not isThreeOfaKind(player1) , 'Should not be ThreeOfaKind, it is a FullHouse!' 

# testcase #18
def test_isTwoPairs_4_cards():
    player1=[('6', 'spades'),  ('5', 'spades'), ('6', 'clubs'), ('5', 'diamonds'), ('2', 'hearts')]
    assert isTwoPairs(player1) , 'Should be TwoPairs!' 
    
# testcase #19
def test_isHighCard_4_card():
    player1=[('10', 'spades'),  ('J', 'spades'), ('9', 'spades'), ('3', 'clubs')]    
    assert isHighCard(player1) , 'Should be HighCard!' 
    
# testcase #20
def test_isHighCard_3_card():
    player1=[('10', 'spades'),  ('K', 'hearts'), ('9', 'diamonds')]
    assert isHighCard(player1) , 'Should be HighCard!' 
    

####################  Assignment 2 #########################

# testcase #21
def test_isFibonacci():
    assert isFibonacci(144), 'Is a isFibonacci!'
    
# testcase #22
def test_isFibonacci_NegatineNumber():
    with pytest.raises(ValueError):
        assert isFibonacci(-144), 'Should not ne negative number!'
        

# testcase #23    
def test_add_even_odd():
    assert add_even_odd([1,2,4,5,6],[10,12,13,15,17,19]) == [17, 23]
    
    
# testcase #24
def test_stripvowels():
    assert stripvowels('tsai') == 'ts'

# testcase #25
def test_relu():
    assert relu([2.0, 1,-0., 5 , -3.2]) == [2,1,0,5,0]
    

# testcase #25
def test_sigmoid():
    assert sigmoid([2.0, 1,-0., 5 , -3.2, -99])[2] == 0.5
    
# testcase #26
def test_charshift():
    assert charshift('123tsaivvvvvv@') == ['y', 'x', 'f', 'n']
    

# testcase #27
def test_findswearwords():
    assert len(findswearwords('paragraph.txt')) > 0
    

# testcase #28
def test_KA_numplates():
    assert len(KA_numplates()) == 15
    

# testcase #29
def test_state_numplates():
    assert len(state_numplates('MH')) == 15    

 
# testcase #30
def test_state_numplates_partial():
    assert len(state_numplates_partial('DL')) == 15        
