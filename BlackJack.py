import random

suits = ["Hearts","Diamomnds","Spades","Clubs"]
ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

playing = True

class Card():
	
	def __init__(self, suit,rank):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return self.rank+" of "+self.suit

class Deck():
	def __init__(self):
		self.deck =[]
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ""
		for card in self.deck:
			deck_comp += "\n"+card.__str__()
		return deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value+=values[card.rank]

	def adjust_for_ace(self):
		while self.value>21 and self.aces:
			self.value-=10
			self.aces-=1

class Chips():
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total+=self.bet

	def lose_bet(self):
		self.total-=self.bet

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet?: "))
		except:
			print("Opps, chips amount shuld be an Intiger...")
		else:
			if chips.bet > chips.total:
				print("Sorry your bet can not exceed {}".format(chips.total))
			else:
				break
def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):

	global playing


	while True:
		x = input("Would you like to Hit or Stand(H/S) ? ")

		if x[0].upper() == "H":
			hit(deck,hand)

		elif x[0].upper() == "S":
			print("Player stands, dealer is playing now")
			playing = False
		else:
			print("Sorry Please try again...")
			continue
		break

def show_some(player,dealer):
	print("\nDealer Hand: ")
	# print("\n<Card hidden>")
	print(" ",dealer.cards[1])
	print("\n Player Hand ",*player.cards,sep = "\n")

def show_all(player,dealer):
	print("\nDealer Hand ",*dealer.cards, sep = "\n")
	print("\nDealer Value: ",dealer.value)

	print("\nPlayer Hand ",*player.cards, sep = "\n")
	print("\nPlayer Value: ",player.value)

def player_busts(player,dealer,chips):
	print("Player busts!")
	chips.lose_bet()

def player_win(player,dealer,chips):
	print("Player wins!")
	chips.win_bet()    

def dealer_busts(player,dealer,Chips):
	print("Dealer busts!")
	# chips.lose_bet()

def dealer_win(player,dealer,chips):
	print("Dealer wins!")
	# chips.win_bet()


while True:

	deck = Deck()
	deck.shuffle()
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	player_chips = Chips()
	take_bet(player_chips)

	show_some(player_hand,dealer_hand)


	while playing:
		hit_or_stand(deck,player_hand)
		show_some(player_hand,dealer_hand)


		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

	if player_hand.value <=21:
		while dealer_hand.value <17:
			print("Dealer HITTT")
			hit(deck,dealer_hand)

		show_all(player_hand,dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_win(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
			player_win(player_hand,dealer_hand,player_chips)

		else:
			push(player_hand,dealer_hand)




	new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
	
	if new_game[0].lower()=='y':
		playing=True
		continue
	else:
		print("Thanks for playing!")
		break


	
	
	

	
	












		
		