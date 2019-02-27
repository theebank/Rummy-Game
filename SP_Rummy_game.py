import random

'Functions needed to' 
def deleting_cards(raw_input,player):
    '''
    (list,list) -> ()
    Goes through each value in the first list,then compares with each value of the second list. If the values line up, deletes the value from the second list.
    '''
    for x in raw_input:
        for y in range(len(player)-1):
            if player[y] == x:
                del player[y]
    return 

def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.
    '''
    unshuffled_deck = []
    for y in range(1,num+1):
        
        for x in range(1,5):
            if int(y) < 10:
                q = str(y)
                q = '0' + q
                r = str(x)+q
                unshuffled_deck.append(r)
            elif int(y) >= 10:
                q = str(y)
                r = str(x)+q
                unshuffled_deck.append(r)
    return unshuffled_deck
                
                

def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck
    '''
    random.shuffle(deck)
    

def deal_cards_start(deck):
    '''(list of int)-> list of int

    Returns a list representing the player's starting hand.
    It is  obtained by dealing the first 7 cards from the top of the deck.
    Precondition: len(dec)>=7
    '''

    player_hand = []
    
    
    deck.reverse()
    for x in range(0,7):
        player_hand.append(deck[0])
        del deck[0]
    deck.reverse()
    return player_hand


def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If len(deck)<num then len(deck) cards is dealt, in particular
    all the remaining cards from the deck are dealt.

    Precondition: 1<=num<=6 deck and player are disjoint subsets of the strange deck. 
    '''
    deck.reverse()
    if len(deck)<num:
        'if the length of the deck is less than number, deal the whole deck'
        for x in range(0,len(deck)):
            player.append(deck[0])
            del deck[0]
    else:
        'asdfds'
        for x in range(0,num):
            player.append(deck[0])
            del deck[0]
    deck.reverse()
    return 

def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    '''
    'making copies of the list'
    temp_player_hand_1 =[]
    temp2 =[]
    for x in hand:
        temp_player_hand_1.append(x)
        temp2.append(x)
    
    'sorting the first temporary list by suit and rank'
    temp_player_hand_1.sort()
    print()
    print("Here is your hand printed in two ways.")
    print()
    print(' '.join(str(x) for x in (temp_player_hand_1)))
    print()
    'sorting the second temporary list by rank'
    temp2.sort()
    def last_letter(s):
        return s[-2:]    
    print(' '.join(str(x) for x in (sorted(temp2,key=last_letter))))
    print()
    
        
    
        
        


def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    '''
    for x in cards:
        for y in player:
            if x == y:
                
                q = 1
                
            else:
                q = 0
        if q == 0:
            return (str(x) + " not in your hand. Invalid input.")
            
        
    return True

def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    '''
    n = 0
    if len(cards) < 2:
        return ("Invalid input. Discardable set needs to have at least 2 cards.")
    elif len(cards) > 4:
        return ("Invalid input. Discardable set needs to have at most 4 cards.")
        
    else:
        x = is_valid(cards,player_hand)
        
        if x == True:
            while n < len(cards):
                if (int(cards[0])%100) == (int(cards[n])%100):
                    n += 1
                else:
                    return False
        else:
            return x
        return True


def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    '''
    playerx = []
    for x in cards:
        playerx.append(x)
    playerx.sort()
    if len(playerx)<3:
        return ("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
    x = is_valid(playerx,cards)    
    if x == True:
        diff = [int(playerx[x+1])-int(playerx[x]) for x in range(len(playerx)-1)]
        for i in diff:
            if i > 20:
                return ("Invalid sequence. Cards are not of same suit.")
            
            if 1< i and i <20:
                return ("Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.")
    else:
        return x
        
    return True

def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck
    '''
    y = True
    q = 0
    print("Discard any card of your choosing.")
    while y:
        raw_input = int(input("Which card would you like to discard?"))
        for x in range(len(player)-1):
            if raw_input != int(player[x]):
                q = 0
            else:
                q = 1
                y = False
                del player[x]
                print_deck_twice(player)
        if q == 0:
            print()
            print("No such card in your hand. Try again.")
    
                
                
        
def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck
    '''
     
    b = True
    while b:
        
        yesno = str(input("Yes or no, do you have a sequence of three or more cards of the same suit or two or more of a kind?")).lower().strip()
        if yesno == 'yes':
            
            raw_input = input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: ").strip().split()
            x = is_discardable_kind(raw_input)
            if x == True:
                deleting_cards(raw_input,player)
                print_deck_twice(player)
            else:
                y= is_discardable_seq(raw_input)
                if y == True:
                    deleting_cards(raw_input,player)
                    print_deck_twice(player)
                else:
                    print(y)

        if yesno == 'no':
            b = False
                


# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
x = True
changed_size = 13
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()
if size_change == 'yes':
    while x:
        changed_size = int(input("Enter a number between 3 and 99 for the number of ranks: "))
        if changed_size > 3 and changed_size < 99:
            x = False
decksize = 4 * changed_size
print("You will be playing with a deck of " + str(decksize) + " cards.")
deck = make_deck(changed_size)
shuffle_deck(deck)
player_hand = deal_cards_start(deck)
print_deck_twice(player_hand)
n=1
while len(player_hand)>1:
    print("Welcome to round " + str(n) + ".")
    print("Please roll the dice.")
    dice_roll = random.randint(1,6)
    print("You roll the dice and it shows: " +str(dice_roll) + ".")
    if dice_roll == 1:
        rolled_one_round(player_hand)
    else:
        print("Since your rolled, " + str(dice_roll) + " the following " + str(dice_roll) + " or " + str(len(deck)) + "(if the deck has less than " + str(dice_roll) + " cards) \nwill be added to your hand from the top of the deck.")
        deal_new_cards(deck,player_hand,dice_roll)
        print_deck_twice(player_hand)
        rolled_nonone_round(player_hand)
    print("Round " + str(n) + " completed.")
    n += 1
print("Welcome to round " + str(n) + ".")
print("The game is in empty deck phase.")
rolled_one_round(player_hand)
print("Round " +str(n) + " completed.")
print("Congratulations, you completed the game in " + str(n) + " rounds.")




  
