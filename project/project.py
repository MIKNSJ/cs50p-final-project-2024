import random
import sys



# player setup
class Player:
    def __init__(self, username, coins):
        self.username = username;
        self.coins = coins;


    def __str__(self):
        return f"\
            \n=================================================== \
            \n| Welcome {self.username}!                          \
            \n| You currently have {self.coins} coins.            \
            \n===================================================";
    

    @property
    def username(self):
        return self._username;


    @property
    def coins(self):
        return self._coins;


    @username.setter
    def username(self, username):
        self._username = username;


    @coins.setter
    def coins(self, coins):
        while (True):
            if (coins > 0):
                break;
            print("The amount of coins deposited should be positive.");
            coins = int(input("Please enter the amount of coins to deposit: "));
        
        self._coins = coins;



# generates a full deck of playing cards
def generate_cards():
    cards = [];

    for i in range(1,53):
        if (i <= 13):
            if (i < 10):
                cards.append(("Hearts", i));
            else:
                cards.append(("Hearts", 10));

        if (i >= 14 and i <= 26):
            if (i < 24):
                cards.append(("Diamonds", i % 13));
            else:
                cards.append(("Diamonds", 10));

        if (i >= 27 and i <= 39):
            if (i < 37):
                cards.append(("Clubs", i % 26));
            else:
                cards.append(("Clubs", 10));

        if (i >= 39 and i <= 51):
            if (i < 49):
                cards.append(("Spades", i % 38));
            else:
                cards.append(("Spades", 10));
    
    # random.shuffle(cards);

    return cards;



# look at the next card
def peek(deck):
    if (len(deck) == 0):
        return f"You cannot call peek on a empty deck!";

    return deck[0];



# find the sum of a hand
def sum_of_hand(deck):
    sum = 0;
    for card in deck:
        if (card[1] == 1 and sum + card[1] <= 21):
            sum += 11;
        else:
            sum += card[1];

    return sum;



# determine the winner of the current hand
def bust(playerHand, cpuHand):
    ...



# prints out a deck of cards
def print_cards(deck):
    for card in deck:
        print(card);
    print(f"Total Cards: {len(deck)}");



# create a player profile
def profile():
    userInput = input("Please enter a username: ");
    depositCoins = input("Please enter the amount of coins to deposit: ");
    return userInput, depositCoins;



# testing environment
def test_envir():
    deck = generate_cards();
    print_cards(deck);
    # empty_deck = [];
    # print_cards(generate_cards());
    #name, coins = profile();
    #player = Player(name, int(coins));
    #print(player.__str__());
    # print(peek(deck));
    print(sum_of_hand(deck));
    # print(peek(empty_deck));



# main function
def main():
    test_envir();



if __name__ == "__main__":
    main();