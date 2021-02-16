import math, urllib,random, string
from functools import reduce,partial
from collections import Counter

suits = ['spades', 'clubs', 'hearts', 'diamonds']
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        

    

def createdeck_LC() -> 'returns list of 52 tuple(val, suite) ':
    ''' creates 52 cards of the suite
    and adds to the deck, using list comprehension
    
    Input:
        None
    Return:
        list of tuple'''       
    
    deck = [(x,y) for x in suits for y in vals]     
    return deck


def createdeck_reg() -> 'list of tuple':
    ''' creates 52 cards vals X suits
    and adds to the deck,using simple for loop.
    Note that above (createdeck_LC) is a LC implementation
    
    Input:
        None
    Return:
        list of tuple'''
        
    deck=[]   
    for s in suits:
       for v in vals:
           deck.append((v,s))     
    return deck  


def createdeck_lambda() -> 'List of tuples':
    ''' Creates 52 cards of the suite and adds to the deck, using lamdba
    
    Input:
        None
        
    Return:
        List of tuples of (value, suite)''' 
        
    return [y for sublist in list(map(lambda x: list(zip(x*4, suits)), vals)) for y in sublist]  
    # following uses simply zip, no map/lambda
    # return list(zip(suits*13, vals*4))  
    
   

##########################################
def _isPerfectSquare(x : 'int >= 0') -> bool:
    ''' Determiones if x is a perfect square
    
    Input:
        x: non-negative integer
    Return:
        True if x is a perfect square, else False''' 
        
     
    s = int(math.sqrt(x)) 
    return s*s == x 
  

def isFibonacci(n: 'int >= 0') -> bool:   
    '''Determines if n is a Fibunacci number.
    n is Fibinacci if  5*n*n + 4 or 5*n*n - 4 is a perferct square  
    
    Input:
        n: non-negative integer
    Return:       
        True if, n is Fibinacci , else False'''
        
    if n < 0:
        raise ValueError('Must be positive number!')  
        
    return _isPerfectSquare(5*n*n + 4) or _isPerfectSquare(5*n*n - 4) 
     
###############################################  

def add_even_odd(l1: 'list of numbers', l2 : 'list of numbers')-> 'list numbers':
    ''' Sums to lists , takes even numbers from one and odd numbers from other
    
     Input:
       l1: list of numbers
       l2: list of numbers
     Return:       
        Sum of (even) l1 + (odd) l2'''
        
    return [z1 + z2 for z1, z2 in zip(l1, l2) if z1 % 2 == 0 and z2 % 2 == 1]
    


def stripvowels(string: str) -> str:
    '''strips every vowel from a string provided
    
     Input:
         str: 
     
     Return:   
         string stripped of vowels'''
         
    #return str([x for x in string if str.upper(x) not in ['A','E','I','O','U']])
    return ''.join([x for x in string if str.upper(x) not in ['A','E','I','O','U']])
   

def relu(l: 'list of number') -> 'list of numbers >= 0':   
     '''Implements RELU funciton
    
     Input:
         list of numbers: 
     
     Return:   
         0, if number < 0
         number, if number >= 0'''   
         
     return( list([x if x >= 0 else 0 for x in l]) )
 
 
def sigmoid(l: 'list of number') -> 'list of numbers between 0 and 1':   
     '''Implements SIGMOID funciton
    
     Input:
          list of numbers: 
     
     Return:   
          number between 0 and 1'''
         
     return list([1/(1 + math.exp(-1*x)) for x in l]) 
 
 
def charshift(string: str) -> str:   
     '''Shifts all characters in string by 5 positions till it falls off alphabet.
     Only ascii alphabet (A_Za-z) is considered
     Also, if after shifting, the ordinal value of the new character is beyond 'z', 
     then it is skipped. 
     So, letter after 'u' would not be shifted.
    
     Input:
         string
     
     Return:   
         string shifted by 5 positions''' 
         
          
     return [chr(ord(x)+5)  for x in string if ord(x) >= ord('A') and ord(x) <= ord('z')-5]
 
    
def _readfile(filename: str, splitchar:str)-> list:
    textfile = open(filename, "r")
    content = textfile.read()  
    text_content_list = content.split(splitchar)
    textfile.close()
    return text_content_list

    
def findswearwords(textfilename: str, swearwordfilename : str ='swearwords.txt')-> bool:
    '''if swearwords from given filename exists in 
    url view-source:https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt.
    Note that, input file 'textfilename' contains paragraph of text.
    Other input file 'swearwordfilename' contains the beautiful words from the given URL
    
    Input:
         string : name of text file
         string : name of text file containing poetic words       
     
    Return:   
         poetic words found in textfile'''  
    return {x for x in  open(textfilename, "r",encoding="utf-8").read().split(' ') if x in  open('swearwords.txt', "r". encoding="utf-8").read().split('\n')}
   
   
def sum_even(l: list)->list:
    '''Sums even numbers in list
    
     Input:         
         list of numbers       
     
     Return:   
         list of even numbers'''  
    return reduce(lambda a, b: (a + b) , list(filter(lambda x: x%2==0, l)))


def findbiggestchar(string: str)->str:
    '''Find biggest character in ascii string
    
    Input:         
         ascii string       
     
    Return:   
         character with max ord()'''  
         
    return reduce(lambda a, b: a if a > b else b , string)


def add3rdNumber(l: 'list of numbers')->'int or float':
    '''Adds every third number in list
    
    Input:         
         list of numbers       
     
    Return:   
         sum of every 3rd number'''  
         
    return reduce(lambda a, b: (a + b) , l[2::3])


def KA_numplates()->'list of string':
    '''Using randint, random.choice and list comprehensions, write an 
    expression that generates 15 random KADDAADDDD number plates, 
    where KA is fixed, D stands for a digit, and A stands for Capital 
    alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
    
    Input:         
         None      
     
    Return:   
         list of 15 strings'''   
         
    return ['KA' + str(random.randint(10, 99)) + 
            "".join(random.choices(string.ascii_uppercase, k = 2)) + 
            str(random.randint(1000, 9999)) for x in range(15)]
    
def state_numplates(state: str, range_start:int = 1000, range_stop:int = 9999)->'list of string':
    '''Using randint, random.choice and list comprehensions, write an 
    expression that generates 15 random KADDAADDDD number plates, 
    where KA is fixed, D stands for a digit, and A stands for Capital 
    alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
    
    Input:         
         state: 2 letter state abbreviation 
         range_start: least number in number plate 
         range_stop: max number in number plate 
     
    Return:   
         list of 15 strings'''   
         
    return [state + str(random.randint(10, 99)) + 
            "".join(random.choices(string.ascii_uppercase, k = 2)) + 
            str(random.randint(range_start, range_stop)) 
            for x in range(15)]


''' partial function'''
state_numplates_partial = partial(state_numplates,range_start=1000,range_stop=9999)


####################### P O K E R #########################


card_value={
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '10':10,
            'J':11,
            'Q':12,
            'K':13,
            'A':14
            }

# assigning weight to ranks (implementation specific)
poker_hand_5_card = { 'RoyalFlush' : 10,
               'StrightFlush' : 9,
               'FourOfaKind' : 8,
               'FullHouse' : 7,
               'Flush' : 6,     #*
               'Straight' : 5,  #*
               'ThreeOfaKind' : 4,
               'TwoPairs' : 3,  #*
               'OnePair' : 2,
               'HighCard' : 1   #*
              }

poker_hand_4_card = {             
               'FourOfaKind' : 8,
               'StrightFlush' : 7,              
               'ThreeOfaKind' : 6,
               'Flush' : 5,     #*
               'Straight' : 4,  #*
               'TwoPairs' : 3,  #*
               'OnePair' : 2,
               'HighCard' : 1   #*
              }

poker_hand_3_card = {                 
               'StrightFlush' : 6,              
               'ThreeOfaKind' : 5,
               'Straight' : 4,  #*
               'Flush' : 3,     #*             
               'OnePair' : 2,
               'HighCard' : 1   #*
              }

def _to_card_numeric_value(cards):     
    return [card_value[x[0]] for x in cards] 

def _to_card_suits(cards):
    return [x[1] for x in cards] 

def isSequence(cards): 
    card_vals = _to_card_numeric_value(cards)
    return sorted(card_vals) == list(range(min(card_vals), max(card_vals)+1)) 

def isSameSuite(cards):     
    return len(set(x[1] for x in cards)) == 1


def isRoyalFlush(cards: 'list of tuple')-> bool:    
    '''The best hand of them all is this famous combination, formed by a 
    Straight Flush that runs to the Ace, making it unbeatable. Odds of being 
    dealt this hand can be as high as 1 in 650,000 deals.
    Example: 10♥ J♥ Q♥ K♥ A♥
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it RoyalFlush'''
    
    return len(cards) == 5 and isSequence(cards) and isSameSuite(cards) and max(_to_card_numeric_value(cards)) == card_value['A']
    

def isStraightFlush(cards: 'list of tuple')-> bool:
    '''Even rarer than four of a kind, a straight flush is made up of 
    five consecutive cards, all from the same suit.
    Example: 9♠ 10♠ J♠ Q♠ K♠
    
     Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it StraightFlush'''
    
    return isSequence(cards) and isSameSuite(cards) and max(_to_card_numeric_value(cards)) != card_value['A']

def isFourOfaKind(cards: 'list of tuple')-> bool:
    '''If you are lucky enough to have all four of a given number, then you have 
    a very powerful hand.
    Example: 9♠ 9♦ 9♥ 9♣ 5♣
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it FourOfaKind'''     
    
    return max(Counter(_to_card_numeric_value(cards)).values()) == 4   
    
    
def isFullHouse(cards: 'list of tuple')-> bool:
    '''When a player has three-of-a-kind and a pair in the same hand, 
    it is called a Full House. 
    Example: 9♠ 9♦ 9♥ 5♣ 5♥
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it isFullHouse'''
    
    temp = sorted(Counter(_to_card_numeric_value(cards)).values(), reverse = True)
    return len(cards) == 5 and temp[0] == 3 and temp[1] == 2
    

def isFlush(cards: 'list of tuple')-> bool:
    '''When all five cards in a hand are of the same suit, it is a flush. 
    If two players have a flush, the person with the highest card in that suit wins.
    Example: 9♠ 5♠ Q♠ K♠ 7♠
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it Flush'''
    
    return isSameSuite(cards) and not isSequence(cards)

def isStraight(cards: 'list of tuple')-> bool:
    ''' A straight is a five-card hand consisting of a running sequence of cards, 
    regardless of suit. If two players have straights, the straight of the higher card wins.
    Example: 9♠ 10♠ J♦ Q♥ K♦
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it Straight'''
    
    return isSequence(cards) and not isSameSuite(cards)


def isThreeOfaKind(cards: 'list of tuple')-> bool:
    '''Example: 9♠ 9♦ 9♥ 5♣ 8♣
    
     Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it ThreeOfaKind'''    

    temp = sorted(Counter(_to_card_numeric_value(cards)).values(), reverse = True)
    if len(cards) == 5:
        return isFlush(cards) == False and temp[0] == 3 and temp[1] == 1
    else:
        return isFlush(cards) == False and temp[0] == 3

       
def isTwoPairs(cards: 'list of tuple')-> bool:
    '''When more than one player has two pairs, the player with the highest pair wins.
    Example: 9♠ 9♦ 5♣ 5♥ 8♥
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it TwoPairs'''
    
    card_vals = _to_card_numeric_value(cards)
    temp = sorted(Counter(card_vals).values(), reverse = True)
    
    return isFlush(cards) == False and temp[0] == 2 and temp[1] ==2
  
def isOnePair(cards: 'list of tuple')-> bool:
    '''A pair is formed when you have two of any of the same cards.
    Example: 9♠ 9♦ 5♣ 8♣ K♥
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it OnePair'''    
    
    card_vals = _to_card_numeric_value(cards)
    temp = sorted(Counter(card_vals).values(), reverse = True)    
    return not isFlush(cards) and temp[0] == 2 and temp[1] != 2

  
def isHighCard(cards: 'list of tuple')-> bool:
    '''If no combination can be made, then a player’s hand is valued at the 
    highest single card. If two players have the same high card, then 
    the second highest card would break the tie.
    Example: 5♣ 8♦ 10♠ Q♥ A♠
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        is it HighCard'''
    
    return  not isRoyalFlush(cards) and \
            not isStraightFlush(cards) and \
            not isFourOfaKind(cards) and \
            not isFullHouse(cards) and \
            not isFlush(cards) and \
            not isStraight(cards) and \
            not isThreeOfaKind(cards) and \
            not isTwoPairs(cards) and \
            not isOnePair(cards)
            
def _tiebreak_sequence(cards1: 'list of numbers' , cards2: 'list of numbers') -> str:    
    ''' If both players have Flush, Straight or HighCard, then 
    from the numeric values of the two sets of cards, 
    decides which set has maximum value (winner)
    
    Input:
        cards1: list of  numbers
        cards2: list of  numbers
          
    Return:
        player1 : if cards1 has higher value than cards2 or vice versa.
        Tie: if both have same value '''
    
    cards1_sorted=sorted(_to_card_numeric_value(cards1), reverse=True)
    cards2_sorted=sorted(_to_card_numeric_value(cards2), reverse=True)    
    for i in range(len(cards1_sorted)):
        if cards1_sorted[i] > cards2_sorted[i]:
            return 'player1'
        elif cards1_sorted[i] < cards2_sorted[i]:
            return 'player2'
        elif i == len(cards1_sorted)-1:
            return 'Tie'
        
def _tiebreak_two_pairs(cards1: 'list of numbers' , cards2: 'list of numbers') -> str: 
    ''' If both players have Two Pairs, then 
    from the numeric values of the two sets of cards, 
    decides which set has maximum value (winner)
    
    Input:
        cards1: list of  numbers
        cards2: list of  numbers
          
    Return:
        player1 : if cards1 has higher value than cards2 or vice versa.
        Tie: if both have same value '''
        
    cards1_freq =Counter(_to_card_numeric_value(cards1))
    cards2_freq =Counter(_to_card_numeric_value(cards2))     
    cards1_sorted=sorted([z for z in cards1_freq if cards1_freq[z] == 2], reverse=True)      
    cards2_sorted=sorted([z for z in cards2_freq if cards2_freq[z] == 2], reverse=True)  
   
    for i in range(len(cards1_sorted)):
        if cards1_sorted[i] > cards2_sorted[i]:
             return 'player1'
        elif cards1_sorted[i] < cards2_sorted[i]:
            return 'player2'
        elif i == len(cards1_sorted)-1:
            return 'Tie'             
               
def _getRank(cards: 'list of tuple')-> str:   
    ''' Determine the rank of a player's cards
    
    Input:
        cards: list of tuples e.g. ('3','diamonds')
          
    Return:
        rank from Poker rules'''
    
    rank = None
    if isRoyalFlush(cards):
        rank = 'RoyalFlush'
    elif isStraightFlush(cards):
        rank = 'StrightFlush'
    elif isFourOfaKind(cards):
        rank = 'FourOfaKind'        
    elif isFullHouse(cards):
        rank = 'FullHouse'
    elif isFlush(cards):
        rank = 'Flush'
    elif isStraight(cards):
        rank = 'Straight'
    elif isThreeOfaKind(cards):
        rank = 'ThreeOfaKind'
    elif isTwoPairs(cards):
        rank = 'TwoPairs'
    elif isOnePair(cards):
        rank = 'OnePair'
    elif isHighCard(cards):
        rank = 'HighCard'
    return rank


def playpoker(player1: 'list of tuple', player2: 'list of tuple') -> str:
    
    '''Simulates the POKER gamne with 3/4/5 cards:
    The ranking of hands, from lowest to highest value:

    High card. If no combination can be made, then a player’s hand is valued at the highest single card. If two players have the same high card, then the second highest card would break the tie.
    Example: 5♣ 8♦ 10♠ Q♥ A♠
    
    One Pair. A pair is formed when you have two of any of the same cards.
    Example: 9♠ 9♦ 5♣ 8♣ K♥
    
    Two Pairs. When more than one player has two pairs, the player with the highest pair wins.
    Example: 9♠ 9♦ 5♣ 5♥ 8♥
    
    Three of a Kind.
    Example: 9♠ 9♦ 9♥ 5♣ 8♣
    
    Straight. A straight is a five-card hand consisting of a running sequence of cards, regardless of suit. If two players have straights, the straight of the higher card wins.
    Example: 9♠ 10♠ J♦ Q♥ K♦
    
    Flush. When all five cards in a hand are of the same suit, it is a flush. If two players have a flush, the person with the highest card in that suit wins.
    Example: 9♠ 5♠ Q♠ K♠ 7♠
    
    Full House. When a player has three-of-a-kind and a pair in the same hand, it is called a Full House.
    Example: 9♠ 9♦ 9♥ 5♣ 5♥
    
    Four of a Kind. If you are lucky enough to have all four of a given number, then you have a very powerful hand.
    Example: 9♠ 9♦ 9♥ 9♣ 5♣
    
    Straight Flush. Even rarer than four of a kind, a straight flush is made up of five consecutive cards, all from the same suit.
    Example: 9♠ 10♠ J♠ Q♠ K♠
    
    Royal Flush. The best hand of them all is this famous combination, formed by a Straight Flush that runs to the Ace, making it unbeatable. Odds of being dealt this hand can be as high as 1 in 650,000 deals.
    Example: 10♥ J♥ Q♥ K♥ A♥
    
    Input:
        player1: list of tuples e.g. ('3','diamonds'), list can contain 3,4 or 5 elements
        player2: list of tuples e.g. ('3','diamonds'), list can contain 3,4 or 5 elements
          
    Return:
        string : plater1 or player2 or Tie '''
        
    poker_hand = None # depends on 3 /4 /5 card game
    if len(player1) == 5:
        poker_hand = poker_hand_5_card
    elif len(player1) == 4:
        poker_hand = poker_hand_4_card
    else:
        poker_hand = poker_hand_3_card
    
    if len(player1) != len(player2):
        raise ValueError('Both players must have same numner of cards!')
    if len(player1) not in [3,4,5]:
        raise ValueError('You can only play with 3, 4 or 5 cards!')
    if len(set(player1 + player2)) != len(player1) + len(player2):
        raise ValueError('Duplicate card detected!')
    player1_score = _getRank(player1)
    player2_score = _getRank(player2)
    print('player1 : ' + player1_score + '\nplayer2 : ' + player2_score)
    winner = None
    if poker_hand[player1_score] > poker_hand[player2_score]:
        winner ='player1'
    elif poker_hand[player1_score] < poker_hand[player2_score]:
        winner ='player2'    
    elif poker_hand[player1_score] == poker_hand[player2_score]:
        if player1_score in ['Flush', 'Straight', 'HighCard']:
            winner = _tiebreak_sequence(player1, player2)
        elif player1_score in ['TwoPairs']:
            winner = _tiebreak_two_pairs(player1, player2)
        else:
            winner = 'Tie'
    return winner       
        
    
'''
print(createdeck_reg())
print(createdeck_lambda())
print(add_even_odd([1,2,4,5,6],[10,12,13,15,17,19]))
print(stripvowels('tSai'))
print(relu([2.0, 1,-0., 5 , -3.2]))
print(sigmoid([2.0, 1,-0., 5 , -3.2, -99])[2])
print(charshift('123tsaivvvvvv@'))
print(findswearwords('cnn.txt',''))
print(sum_even([1,2,3,4,5,6,7,-2]))
print(findbiggestchar('23ABxFCDYZ'))
print(add3rdNumber([1,2,3,4,5,6,7,8,9,10]))
print(KA_numplates())
print(state_numplates('AS',10,99))
print(state_numplates_partial('MH'))
'''
'''
cards1=[('A', 'spades'),  ('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]

cards2=[('9', 'spades'),  ('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]
cards2_1=[ ('10', 'spades'), ('Q', 'spades'), ('J', 'spades')]

cards3=[('10', 'spades'),  ('J', 'spades'), ('10', 'hearts'), ('10', 'clubs'), ('10', 'diamonds')]
cards3_1=[('10', 'spades'),  ('10', 'clubs'), ('10', 'diamonds')]

cards4=[('10', 'spades'),  ('J', 'hearts'), ('J', 'spades'), ('10', 'clubs'), ('10', 'diamonds')]
cards4_1=[ ('J', 'hearts'), ('J', 'spades'), ('10', 'clubs'), ('10', 'diamonds')]

cards5=[('10', 'hearts'),  ('J', 'hearts'), ('4', 'hearts'), ('6', 'hearts'), ('7', 'hearts')]
cards5_1=[('A', 'spades'),  ('10', 'spades'), ('K', 'spades'), ('Q', 'spades'), ('J', 'spades')]


cards6=[('10', 'spades'),  ('J', 'spades'), ('9', 'clubs')]

cards7=[('6', 'spades'),  ('5', 'spades'), ('6', 'clubs'), ('6', 'diamonds'), ('5', 'hearts')]

cards8=[('6', 'spades'),  ('4', 'herats'), ('6', 'diamonds'), ('4', 'spades')]
cards8_1=[('6', 'spades'),  ('4', 'herats'), ('6', 'diamonds'), ('4', 'spades'), ('K', 'spades')]

cards9=[('6', 'spades'),  ('4', 'spades'), ('3', 'spades'), ('6', 'clubs'), ('5', 'spades')]
cards9_1=[('6', 'spades'),  ('4', 'diamonds'), ('6', 'diamonds')]

cards10=[('6', 'spades'),  ('4', 'spades'), ('3', 'spades'), ('8', 'spades'), ('5', 'clubs')]

cards01 = [('8', 'spades'),  ('J', 'diamonds'), ('4', 'hearts'),('5', 'clubs')]
cards02 = [('4', 'hearts'),  ('8', 'spades'), ('J', 'clubs'), ('9', 'clubs')]

cards_tp_1 = [('8', 'spades'),  ('10', 'clubs'), ('Q', 'diamonds'), ('8', 'hearts'),('10', 'spades')]
cards_tp_2 = [('8', 'hearts'),  ('8', 'clubs'), ('J', 'diamonds'), ('K', 'hearts'), ('J', 'spades')]

cards11=[('10', 'spades'),  ('J', 'spades'), ('9', 'spades'), ('Q', 'spades')]
cards11_1=[('6', 'hearts'),  ('6', 'spades'), ('6', 'diamonds'), ('6', 'clubs')]

cards = cards01

print('isRoyalFlush =',isRoyalFlush(cards))
print('isStraightFlush =',isStraightFlush(cards))
print('isFourOfaKind =', isFourOfaKind(cards))
print('isFullHouse =', isFullHouse(cards))
print('isFlush =', isFlush(cards))
print('isStraight =',  isStraight(cards))
print('isThreeOfaKind =', isThreeOfaKind(cards))
print('isTwoPairs =', isTwoPairs(cards))
print('isOnePair =', isOnePair(cards))
print('isHighCard =', isHighCard(cards))
print("\n\n")

print('_tiebreak_sequence = ', _tiebreak_sequence(cards01, cards02))
print('_tiebreak_two_pairs = ', _tiebreak_two_pairs(cards_tp_1, cards_tp_2))



player1=[('3', 'spades'), ('5', 'clubs'), ('4', 'diamonds')]
player2=[('7', 'spades'), ('9', 'clubs'), ('10', 'diamonds')]
print('winner: ' + playpoker(player1, player2))
'''

