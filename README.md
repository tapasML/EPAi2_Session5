# EPAi2_Session5

# Assignment 1:

1. Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts

  # createdeck_lambda() 

2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts

  # createdeck_reg()  : uses for loop
  # createdeck_LC : additional function using LC

3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker (Links to an external site.)! - 150 pts

  # playpoker(player1: 'list of tuple', player2: 'list of tuple')
  
  function returns: 'player1' if player1 wins
                    'player2' if player2 wins
                    'Tie' if there is a tie
                    
 ## Note:
 
  On this Poker simulation, a card is simulated as a tuple e.g. ('A', 'spades')
  
  card values are ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  
  card suits are  ['spades', 'clubs', 'hearts', 'diamonds']
  
 Program looks for tie only in case of (Flush/ Straight/ Two Pairs/ HighCard). 
 
 In other words, for For RoyalFlush, StraightFlush, FourOfaKind, FullHouse, ThreeOfaKind, OnePair  if both pair has same rank, then program decalres a tie.
 
 5 Card Poker rules reference:  https://www.considerable.com/entertainment/card-games/basic-poker/
 
 4 Card Poker rules reference:  https://www.888poker.com/magazine/strategy/4-card-poker
 
 3 Card Poker rules reference:  https://en.wikipedia.org/wiki/Three_Card_Poker
  
  
  
# Assignment 2 

1.   Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:100

  # isFibonacci(n: 'int >= 0') -> bool:  
  
  Note: Fibunacci number can be determined by checking if  5*n*n + 4 or 5*n*n - 4 is a perferct square, no need to store the series.  


2.  Using list comprehension (and zip/lambda/etc if required) write an expression that: 

      1. add 2 iterables a and b such that a is even and b is odd
      
       # add_even_odd(l1: 'list of numbers', l2 : 'list of numbers')-> 'list numbers'
       
        
      2. strips every vowel from a string provided (tsai>>t s)
      
       # stripvowels(string: str) -> str:
       
       
      3. acts like a ReLU function for a 1D array
      
       # relu(l: 'list of number') -> 'list of numbers >= 0': 
       
               
      4. acts like a sigmoid function for a 1D array
      
       # sigmoid(l: 'list of number') -> 'list of numbers between 0 and 1':
       
               
      5 takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
      
       # charshift(string: str) -> str:   
        
    
3. A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt 

      # findswearwords(textfilename: str, swearwordfilename: str)-> bool:
      
      Note: The swearwords from the external file are stored local file 'swearwordfilename' and
      the 200+ words paragraph is stored in local file 'textfilename'.
      The file names are passed as argument


4.  Using reduce function: 

    1. add only even numbers in a list
    
      # sum_even(l: list)->list:
        
        
    2. find the biggest character in a string (printable ascii characters)
    
      # findbiggestchar(string: str)->str:
      
      
    3. adds every 3rd number in a list
    
      # add3rdNumber(l: 'list of numbers')->'int or float':
      
     
    
        
5.  Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

      # KA_numplates()->'list of string':
      
      
6.   Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided

      #  state_numplates(state: str, range_start:int = 1000, range_stop:int = 9999)->'list of string':


    

 


