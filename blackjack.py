# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
player_hand = []
dealer_hand = []
win = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
score = "the score is: " + str(win)

# define card class

    

class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.list = list()
            # create Hand object

    def __str__(self):
        ans = ""
        for i in range(len(self.list)):
            ans += str(self.list[i]) + " "
        return "The cards on hand is:" + ans
            
            # return a string representation of a hand

    def add_card(self, card):
        self.list.append(card)
            # add a card object to a hand

    def get_value(self):
        value = 0
        for i in range(len(self.list)):
            value += VALUES[self.list[i].get_rank()]
        for card in self.list:
            if card.get_rank() == 'A' and value + 10 <= 21:
                value += 10
        return value
                
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for card in self.list:
            card.draw(canvas, pos)
            # draw a hand on the canvas, use the draw method for cards
    
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.list = list()
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                card = Card(SUITS[i], RANKS[j])
                self.list.append(card)
        
        
            # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.list)
            # use random.shuffle()

    def deal_card(self):
        card_deal = self.list.pop()
        return card_deal
        self.list.pop()
        
            # deal a card object from the deck
    
    def __str__(self):
        ans = ""                   
        for card in self.list:
            ans += str(card) + " "
        return "deck contains: " + ans 


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand,newdeck, win
    if in_play:
        win -=1
        outcome = "wrong action so you lose"
    else:  
        newdeck = Deck()
        newdeck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(newdeck.deal_card())
        dealer_hand.add_card(newdeck.deal_card())
        player_hand.add_card(newdeck.deal_card())
        dealer_hand.add_card(newdeck.deal_card())
        outcome = "player has: " + str(player_hand) + "dealer has: " + str(dealer_hand)
        # your code goes here

        in_play = True

def hit():
        # replace with your code below
    global newdeck, outcome, player_hand, win, in_play
    # if the hand is in play, hit the player
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(newdeck.deal_card())
            outcome = "player has: " + str(player_hand) + "dealer has: " + str(dealer_hand)
        elif player_hand.get_value() > 21:
            outcome = "you have busted"
            win -= 1
            in_play = False
            
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, player_hand, dealer_hand, win, score, in_play
        # replace with your code below
    if in_play:
        if player_hand.get_value() > 21:
            print "please notice you have busted"
        else:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(newdeck.deal_card())
            if dealer_hand.get_value() > 21:
                outcome = "dealer has busted"
                win += 1
                in_play = False
            else:	
                if dealer_hand.get_value() >= player_hand.get_value():
                    outcome = "dealer win"
                    win -= 1
                    in_play = False
                
                else:
                    outcome = "player win"
                    win += 1
                    in_play = False
                
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    
    # test to make sure that card.draw works, replace with your code below
    global player_hand, outcome, in_play,score
    
    
    canvas.draw_text("The player has:", (80,90), 18, "Red")
    canvas.draw_text("The dealer has:", (80,290), 18, "Red")
    for i in range(len(player_hand.list)):
        if len(player_hand.list) <= 5:
            player_hand.list[i].draw(canvas, (100 + i * 72,100))
    
    for i in range(len(dealer_hand.list)):
        if len(dealer_hand.list) <= 5:
            dealer_hand.list[i].draw(canvas, (100 + i * 72,300))
    canvas.draw_text(outcome, (20,50), 12, "White")
    canvas.draw_text("blackjack", (100, 30), 30, "Red")
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, (136, 348), CARD_SIZE)
    canvas.draw_text("the score is : " + str(win), (350,500), 20, "Black")
        
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()



# remember to review the gradic rubric