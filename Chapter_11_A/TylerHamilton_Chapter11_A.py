# write a game program that deals a Poker hand of five cards. 
# Then prompt the user to enter a series of numbers (for example: 1, 3, 5) that selects cards to be replaced during a draw phrase. 
# Then print the result of drawing the new cards.
import random

class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)
    
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card
    
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()
        

def main():
    # Ask the user if they wish to play Poker or not.
    choice = input('Would you like to play a game of Poker? ')
    
    if choice.lower() == 'yes':
        # Create a Deck object with a size of 52 cards.
        deck = Deck(52)
        
        # Five cards in a hand of Poker.
        num_cards_in_hand = 5
        
        # Initialize a list to hold the current cards in hand. 
        cards_in_hand_list = []
        
        # Create 5 different cards for the current cards in hand.
        for i in range(num_cards_in_hand):
            # Temporary variable to hold each card as it is chosen.
            card = deck.deal()
            # Append each card to the list of cards in hand
            cards_in_hand_list.append(card)
            # Display the cards on the same line for the user.
            print(card, end=' ')

        # Get the cards the user wishes to exchange.
        cards_to_exchange = input('\nWhich cards would you like to exchange? (Please separate the card indexes by commas):')
        
        # Split the string of card indexes into a list.
        card_idx_to_exchange_list = cards_to_exchange.split(',')
        card_idx_to_exchange_list = [int(item) for item in card_idx_to_exchange_list]
        
        # Loop to remove the cards and exchange them for new cards
        for k in card_idx_to_exchange_list:
            # Remove the selected card from the cards in hand list.
            cards_in_hand_list.pop(int(k) - 1)
            # Add a freshly drawn card to the cards in hand list.
            cards_in_hand_list.insert(int(k) - 1, deck.deal())
            
        # Clear the cards to exchange list.
        card_idx_to_exchange_list.clear()
        
        # Iterate through the cards in hand to print them to the terminal.
        for i in cards_in_hand_list:
        
            # Display the final result of the cards, after a drawing phase.
            print(i, end=' ')
        deck.new_hand()
    # If the user enters "no", then quit.
    elif choice.lower() == 'no':
        quit()
    # If the user does not enter yes or no, request them to try again.
    else:
        print('Please enter "yes" to play or "no" to quit.')
        main()
        
if __name__ == '__main__':
    main()
