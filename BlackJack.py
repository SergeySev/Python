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
score = 0
massage = ""
player_score = 0
diler_score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
player_value = 0
player_hand = 0
play_deck = 0
diler_hand = 0
diler_value = 0

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
        

class Hand:
    def __init__(self):
        self.cards = []	
        
    def __str__(self):
        printed = ""
        for card in self.cards:
            printed += " " + str(card)
        return "Hand contains" + printed

    def add_card(self, card):
        self.cards.append(card)	

    def get_value(self):
        value = 0
        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]
        if rank == "A" and value < 11:
            value += 10
        return value
        
    def draw(self, canvas, pos):
        for c in self.cards:
            c.draw(canvas, pos)	
            pos[0] += 80
            
      
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self): 
        random.shuffle(self.cards)  

    def deal_card(self):
        rand_index = random.randrange(0, (len(self.cards) - 1))
        return self.cards.pop(rand_index)
    
    def __str__(self):
        return "Deck contains" + str(self.cards)


#define event handlers for buttons
def deal():
    global outcome, in_play, player_value, player_hand, play_deck
    global diler_value, diler_hand, massage, in_play, player_score, diler_score
    massage = ""
    
    if in_play:
        massage = "You've given up."
        outcome = "New Deal?"
        diler_score += 1
        in_play = False
        
    else:
        massage = ""
        play_deck = Deck()
        play_deck.shuffle()

        # player deal cards
        player_hand = Hand()
        player_hand.add_card(play_deck.deal_card())
        player_hand.add_card(play_deck.deal_card())
        player_value = player_hand.get_value()

        # diler deal cards
        diler_hand = Hand()
        diler_hand.add_card(play_deck.deal_card())
        diler_hand.add_card(play_deck.deal_card())
        diler_value = diler_hand.get_value()

        in_play = True
        outcome = "Hit or stand?"
    
    
def hit():
    global player_value, player_hand, play_deck, diler_hand
    global outcome, massage, in_play, player_score, diler_score
    
    player_value = player_hand.get_value()
    if in_play:
        if player_value <= 21:
            player_hand.add_card(play_deck.deal_card())
            player_value = player_hand.get_value()

    player_value = player_hand.get_value()
    if in_play:
        if player_value > 21:
            massage = "You have busted"
            in_play = False
            diler_score += 1
       
def stand():
    global player_value, player_hand, play_deck, diler_hand
    global diler_value, outcome, massage, in_play, diler_score, player_score
    
    player_value = player_hand.get_value()
    if in_play:
        if player_value > 21:
            massage = "You have busted"
            in_play = False
            print diler_hand
            diler_score += 1
            
    diler_value = diler_hand.get_value()
    if in_play:
        while diler_value < 17:
            diler_hand.add_card(play_deck.deal_card())
            diler_value = diler_hand.get_value()

    if in_play:    
        diler_value = diler_hand.get_value()
        if diler_value > 21:
            massage = "You win!!!"
            outcome = "New Deal?"
            in_play = False
            player_score += 1

        elif player_value > diler_value:
            massage = "You win!!!"
            outcome = "New Deal?"
            in_play = False
            player_score += 1

        elif player_value == diler_value:
            massage = "Diller win!!!"
            outcome = "New Deal?"
            in_play = False
            diler_score += 1

        else:
            massage = "Diller win!"
            outcome = "New Deal?"
            in_play = False
            diler_score += 1

            
def draw(canvas):
    global player_value, player_hand, play_deck, diler_hand
    global diler_value, outcome, massage, player_score, diler_score
     
    player_hand.draw(canvas, [100, 300])
    diler_hand.draw(canvas, [100, 150])
    
    canvas.draw_text('BlackDjeck', (270, 50), 40, 'Red')
    canvas.draw_text(str(outcome), [270, 120], 40, 'White')
    canvas.draw_text(str(massage), [250, 280], 30, 'White')
    canvas.draw_text("Player Score " + str(player_score), [10, 290], 30, 'Black')
    canvas.draw_text("Diler Score " + str(diler_score), [10, 140], 30, 'Black')

    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (135, 200), CARD_BACK_SIZE)


frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
frame.set_draw_handler(draw)


deal()
frame.start()
