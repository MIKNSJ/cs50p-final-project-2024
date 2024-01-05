import random
import sys



# table setup
class Table:
    def __init__(self):
        self.player_hand = [];
        self.cpu_hand = [];
        self.cpu_hidden_hand = [];


    def flush(self):
        self.player_hand.clear();
        self.cpu_hand.clear();
        self.cpu_hidden_hand.clear();



# player setup
class Player:
    def __init__(self, username, coins):
        self.username = username;
        self.coins = coins;


    def __str__(self):
        return f"\
            \n============================================================= \
            \n     Welcome {self.username}!                                 \
            \n                                                              \
            \n     You currently have {self.coins} coin(s)!                 \
            \n=============================================================\n";


    # player makes a bet
    def place_bet(self):
        while (True):
            try:
                bet = float(input("[SYSTEM]: Please enter the amount to "
                                  "bet: "));

                if (bet > 0 and bet <= self._coins):
                    print(f"[SYSTEM]: You have placed a bet of"
                          " amount: {bet}.");
                    break;

                print("[SYSTEM]: You do not have this amount of coins.");

            except (ValueError):
                print("[SYSTEM]: REQUEST DENIED\n"
                      "The bet amount is not numeric.");
                pass;
       
        self._coins -= bet;

        return bet;


    # payout
    def payout(self, bet, winner):
        if (winner == "player"):
            print("[SYSTEM]: You have won!");
            self._coins += 1.5 * bet;
        
        elif (winner == "cpu"):
            print("[SYSTEM]: You have lost...");
    
        else:
            print("[SYSTEM]: You have tied.");
            self.coins += bet;
    
    # write to results
    def write_results(self, file, bet, result):
        if (result == "player"):
            file.write(f"Won, Payout: {1.5 * bet}, Coins: {self._coins}\n");
        
        elif (result == "cpu"):
            file.write(f"Lost, Payout: {-1 * bet}, Coins: {self._coins}\n");
        
        else:
            file.write(f"Tied, Payout: {bet}, Coins: {self._coins}\n");


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
        self._coins = coins;



# actions
def actions():
    action = input("Player moves = \n"
                    "1. h/hit/draw\n"
                    "2. stand/stn\n"
                    "3. split\n"
                    "4. swap/sp\n"
                    "5. dd\n"
                    "6. special\n"
                    "7. peek\n\n"
                    "Enter the exact move name: ").strip().lower();

    if (action == "h" or action == "hit" or action == "draw"):
        return 0;
    elif (action == "stand" or action == "stn"):
        return 1;
    elif (action == "split"):
        return 2;
    elif (action == "swap" or action == "sp"):
        return 3;
    elif (action == "dd" or action == "double down" or action == "dbldn"):
        return 4;
    elif (action == "special"):
        return 5;
    elif (action == "peek"):
        return 6;
    else:
        print("[SYSTEM]: Please enter a valid move.");
        return -1;



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
    
    random.shuffle(cards);

    return cards;



# draw a card
def draw(deck):
    if (len(deck) == 0):
        print("[TABLE]: The deck is empty!")
        return "exit";

    card = deck.pop(0);
    return deck, card;



# look at the next card
def peek(deck):
    if (len(deck) == 0):
        print("[SYSTEM]: You cannot call peek on a empty deck!")
        return "exit";

    return deck[0];



# swap decks
def swap(deckOne, deckTwo):
    print("\n[TABLE]: Swap has commensed.\n");
    return deckTwo, deckOne;



# obtain special cards
def special_cards(hand):
    special = [("Circle", -1), ("Rectangle", -2), ("Triangle", -3),
               ("Square", -4), ("Pentagon", -5)];
    
    for card in hand:
        if (card[1] < 0):
            print("\n[SYSTEM]: You can only have one special card in"
                  " your hand!\n");
            return "exit";

    special_card = random.choice(special);
    hand.append(special_card);
    print("\n[TABLE]: Card has been added.\n");

    return hand;



# split
def split(hand):
    if (len(hand) < 2):
        print("\n[SYSTEM]: You cannot call split on a hand with less than two"
              " cards!\n");
        return "exit";

    elif (len(hand) > 2):
        print("\n[SYSTEM]: You cannot call split on a hand with greater than two"
              " cards!\n");
        return "exit";

    elif (hand[0][1] != hand[1][1]):
        print("\n[SYSTEM]: You cannot call split on two non-equal cards!\n");
        return "exit";

    else:
        split_hand_left = [hand[0]];
        split_hand_right = [hand[1]];

        return split_hand_left, split_hand_right;



# find the sum of a hand
def sum_of_hand(hand):
    sum = 0;
    for card in hand:
        if (card[1] == 1 and sum + 11 <= 21):
            sum += 11;
        else:
            sum += card[1];

    return sum;



# determine the winner of the current hand
def bust(sumPlayerHand, sumCpuHand):
    if (sumPlayerHand > 21 and sumCpuHand <= 21):
        return "cpu";

    elif (sumPlayerHand <= 21 and sumCpuHand > 21):
        return "player";

    elif (sumPlayerHand == 21 and sumCpuHand != 21):
        return "player";

    elif (sumPlayerHand != 21 and sumCpuHand == 21):
        return "cpu";

    elif (sumPlayerHand > 21 and sumCpuHand > 21):
        return "cpu";
    
    elif (sumPlayerHand > sumCpuHand):
        return "player";

    elif (sumPlayerHand < sumCpuHand):
        return "cpu";

    else:
        return "neither";



# prints out a deck of cards
def print_cards(deck):
    for card in deck:
        print(card);
    print(f"Total Cards = {len(deck)}");



# prints out a hand
def print_hand(hand, user):
    print(f"==================== {user} ==========================================================================\n");
    for card in hand:
        print(card, end=" ");
    print(f"\n\nSum = {sum_of_hand(hand)}");
    print(f"Cards = {len(hand)}\n");
    print(f"======================================================================================================\n");
    print(f"\n\n");



# prints out with hidden hand
def print_hidden_hand(hand, hiddenHand, user):
    print(f"==================== {user} ==========================================================================\n");
    for card in hiddenHand:
        print(card, end=" ");
    
    if (hiddenHand[0][1] == 1):
        print(f"\n\nSum = 11+ ")

    else:
        print(f"\n\nSum = {hiddenHand[0][1]}+ ");

    print(f"Cards = {len(hand)}\n");
    print(f"======================================================================================================\n");
    print(f"\n\n");



# create a player profile
def profile():
    userInput = input("[SYSTEM]: Set a username: ");

    while (True):
        try:
            depositCoins = float(input("[SYSTEM]: Enter playing amount: "));
            break;

        except (ValueError):
            print("[SYSTEM]: REQUEST DENIED.\nPlease enter the amount of coins "
                   "numerically and try again.");
            pass;
    
    while (depositCoins < 1):
        print("[SYSTEM]: The amount of coins deposited should be positive.");
        depositCoins = float(input("[SYSTEM]: Please enter the amount of coins "
                                   "to deposit: "));

    return userInput, depositCoins;



# create the game
def game():
    print("\n[SYSTEM]: Loading Blackjack...");

    with open("log.txt", "w") as file:
        deck = generate_cards();
        table = Table();
        name, coins = profile();
        player = Player(name, int(coins));
        start_amount = player.coins;
        file.write(f"Username: {player.username}\nCoins: {player.coins}\n\n");
        print(player.__str__());

        userInput = input("[SYSTEM]: Type quit or anything"
                          " to play: ").strip().lower();
        
        while (userInput != "quit"):
            if (len(deck) == 0):
                deck = generate_cards();
                print("[TABLE]: The deck has been refreshed.");
            
            bet = player.place_bet();
            file.write(f"Bet: {bet}, Coins: {player.coins}\n");
            print(f"[SYSTEM]: Your new balance is {player.coins} coins."); 
            print(f"[SYSTEM]: Setting up table...");

            divide = False;
            peeked = False;
            left_peek = False;
            right_peek = False;
            left_dbl = False;
            right_dbl = False;
            swapped = False;
            left_swap = False;
            right_swap = False;
            left_bet = 0;
            right_bet = 0;

            deck, card = draw(deck);
            table.player_hand.append(card);
            deck, card = draw(deck);
            table.cpu_hand.append(card);
            table.cpu_hidden_hand.append(card);
            deck, card = draw(deck);
            table.player_hand.append(card);
            deck, card = draw(deck);
            table.cpu_hand.append(card);
            table.cpu_hidden_hand.append(f"(?)");

            print(f"\n\n\n");
            print(f"Coins = {player.coins}");

            if (left_bet > 0):
                print(f"Left Bet = {left_bet}, Right Bet = {right_bet}");
            
            else:
                print(f"Bet = {bet}\n");
            
            print(f"\nCards remaining = {len(deck)}");
            print_hidden_hand(table.cpu_hand, table.cpu_hidden_hand, "CPUBot");
            print_hand(table.player_hand, "Player");

            if (sum_of_hand(table.player_hand) != 21):
                while (True):
                    userAction = actions();

                    # hit
                    if (userAction == 0):
                        if (len(deck) == 0):
                            print("[TABLE]: There is no more cards in the deck!");
                            break;
                        
                        if (divide == False):
                            deck, card = draw(deck);
                            table.player_hand.append(card);

                            if (sum_of_hand(table.player_hand) >= 21):
                                break;

                        else:
                            if (len(deck) <= 1):
                                break;
                            
                            side = input("[SYSTEM]: Type h1 or h2 to draw a "
                                "card on that hand: ").strip().lower();
                            
                            if (left_dbl == False):
                                if (side == "h1"):
                                    if (sum_of_hand(left) < 21):
                                        deck, card = draw(deck);
                                        left.append(card);

                                    else:
                                        print(f"[TABLE]: Left side has "
                                            "exceeded 21");
                            
                            else:
                                print("\n[TABLE]: You cannot perform this action "
                                    "due to a dbl down.");
                            
                            if (right_dbl == False):
                                if (side == "h2"):
                                    if (sum_of_hand(right) < 21):
                                        deck, card = draw(deck);
                                        right.append(card);

                                    else:
                                        print(f"[TABLE]: Right side has exceeded"
                                            " 21");

                                if (sum_of_hand(left) >= 21 and
                                    sum_of_hand(right) >= 21):
                                    break;

                            else:
                                print("\n[TABLE]: You cannot perform this action "
                                    "due to a dbl down.");
                    
                    # stand
                    if (userAction == 1):
                        break;
                    
                    # split
                    if (userAction == 2):
                        if (divide == False):
                            if (split(table.player_hand) != "exit"):
                                left, right = split(table.player_hand);
                                divide = True;
                                left_bet = bet / 2.0;
                                right_bet = bet / 2.0;
                            
                        else:
                            print("[TABLE]: You have already split. Limit = 1.\n");

                    # swap
                    if (userAction == 3):
                        if (divide == False):
                            if (swapped == False):
                                table.player_hand, table.cpu_hand = swap(
                                    table.player_hand, table.cpu_hand);

                                table.cpu_hidden_hand.clear();
                                for i in range(len(table.cpu_hand)):
                                    if (i == 0):
                                        table.cpu_hidden_hand.append(
                                            table.cpu_hand[i]);
                                    
                                    else:
                                        table.cpu_hidden_hand.append("(?)");

                                swapped = True;
                            
                            else:
                                print("\n[TABLE]: You have already swapped! "
                                    "Limit = 1.\n");

                        else:
                            side = input("[SYSTEM]: Type sp1 or sp2 to swap a the "
                                        "left or right deck "
                                        "with the CPU: ").strip().lower();

                            if (left_dbl == False):
                                if (left_swap == False):
                                    if (side == "sp1"):
                                        left, table.cpu_hand = swap(left,
                                                                    table.cpu_hand);

                                        table.cpu_hidden_hand.clear();
                                        for i in range(len(left)):
                                            if (i == 0):
                                                table.cpu_hidden_hand.append(
                                                    left[i]);
                                            
                                            else:
                                                table.cpu_hidden_hand.append("(?)");

                                    left_swap = True;
                                
                                else:
                                    print("[TABLE]: You have already swapped on "
                                        "the left side! Cannot swap again.\n");
                            
                            else:
                                print("\n[TABLE]: You cannot perform this action "
                                    "due to a dbl down.");

                            if (right_dbl == False):
                                if (right_swap == False):
                                    if (side == "sp2"):
                                        right, table.cpu_hand = swap(
                                            right, table.cpu_hand);

                                        table.cpu_hidden_hand.clear();
                                        for i in range(len(left)):
                                            if (i == 0):
                                                table.cpu_hidden_hand.append(
                                                    right[i]);
                                            
                                            else:
                                                table.cpu_hidden_hand.append("(?)");

                                    right_swap = True;
                                
                                else:
                                    print("[TABLE]: You have already swapped on "
                                        "the right! Cannot swap again.\n");

                            else:
                                print("\n[TABLE]: You cannot perform this action "
                                    "due to a dbl down.");

                    # double down
                    if (userAction == 4):
                        if (divide == False):
                            if (len(deck) == 0):
                                print("\n[TABLE]: There is no more cards in the "
                                    "deck!\n");
                                break;
                            
                            if (bet * 2 < player.coins):
                                deck, card = draw(deck);
                                table.player_hand.append(card);
                                player._coins -= bet;
                                bet*=2;
                                left_bet*=2;
                                right_bet*=2;
                                print("\n[TABLE]: Double down active, check "
                                    "your new bet and balance.\n")
                            
                            else:
                                print("\n[TABLE]: You do not have enough coins "
                                    "to double down.\n");
                            
                            break;

                        else:
                            if (len(deck) <= 1):
                                break;

                            side = input("[SYSTEM]: Type dd1 or dd2 to dbl down "
                                        "on that hand: ").strip().lower();

                            if (left_dbl == False):
                                if (side == "dd1"):
                                    if (sum_of_hand(left) < 21):
                                        if (left_bet * 2 < player._coins):
                                            deck, card = draw(deck);
                                            left.append(card);
                                            left_dbl = True;
                                            player._coins -= left_bet;
                                            left_bet*=2;
                                            print("[TABLE]: Double down on left "
                                                "active check your new bet "
                                                "and balance");

                                        else:
                                            print("[TABLE]: You do not have enough "
                                                "coins to double down.");

                                    else:
                                        print(f"[TABLE]: Left side has exceeded "
                                            "21");
                            
                            else:
                                print("\n[TABLE]: You cannot perform this action "
                                    "due to a dbl down.");
                            
                            if (right_dbl == False):
                                if (side == "dd2"):
                                    if (sum_of_hand(right) < 21):
                                        if (right_bet * 2 < player._coins):
                                            deck, card = draw(deck);
                                            right.append(card);
                                            right_dbl = True;
                                            player._coins -= right_bet;
                                            right_bet*=2;
                                            print("[TABLE]: Double down on right "
                                                "active, check you new bet "
                                                "and balance");

                                    else:
                                        print(f"[TABLE]: Right side has exceeded "
                                            "21");
                            
                            else:
                                print("\n[TABLE]: You cannot perform this action "
                                    "due to a dbl down.");

                            if (sum_of_hand(left) >= 21 and
                                sum_of_hand(right) >= 21):
                                break;

                    # special cards
                    if (userAction == 5):
                        if (divide == False):
                            special_cards(table.player_hand);
                        else:
                            side = int(input("[SYSTEM]: Type sp1 or sp2 to draw a "
                                            "card on that hand: "));

                            if (side == "sp1"):
                                print("\n[TABLE]: Card has been added to the "
                                      "left deck\n");
                                special_cards(left);
                            
                            if (side == "sp2"):
                                print("\n[Table]: Card has been added to the "
                                      "right deck\n");
                                special_cards(right);
                    
                    # peek
                    if (userAction == 6):
                        if (divide == False):
                            if (peeked == False):
                                print(f"\n[TABLE]: PEEKED CARD = {peek(deck)}\n");
                                peeked = True;
                        
                            else:
                                print(f"\n[TABLE]: You have already peeked. "
                                    "Limit = 1.\n");
                    
                        else:
                            if (left_dbl == False):
                                if (left_peek == False):
                                    print(f"\n[TABLE]: PEEKED CARD 1 = "
                                        "{peek(deck)}\n");
                                
                                else:
                                    print("[TABLE]: You have already peeked the "
                                        "left deck. Limit = 1");
                            else:
                                print("\n[TABLE]: You cannot perform this action "
                                        "due to a dbl down.");
                                
                            if (right_dbl == False):
                                if (right_peek == False):
                                    print(f"\n[TABLE]: PEEKED CARD 2: "
                                        "{peek(deck)}\n");
                                
                                else:
                                    print("\n[TABLE]: You cannot perform this "
                                        "action due to a dbl down.");
                    
                    if (left_dbl == True and right_dbl == True):
                        break;
                    
                    if (divide == False):
                        print(f"Coins = {player.coins}");
                        print(f"Bet = {bet}\n");
                        print(f"Cards remaining = {len(deck)}");
                        print_hidden_hand(table.cpu_hand,
                                        table.cpu_hidden_hand, "CPUBot");
                        print_hand(table.player_hand, "Player");

                    else:
                        print(f"Coins = {player.coins}");
                        print(f"Left Bet = {left_bet}, Right Bet = {right_bet}");
                        print(f"Cards remaining = {len(deck)}");
                        print_hidden_hand(table.cpu_hand,
                                        table.cpu_hidden_hand, "CPUBot");
                        print_hand(left, "Player-Left");
                        print_hand(right, "Player-Right");
            
            while (sum_of_hand(table.cpu_hand) < 17):
                if (len(deck) == 0):
                    break;
                
                deck, card = draw(deck);
                table.cpu_hand.append(card);
                table.cpu_hidden_hand.append("(?)");
                print(f"\n\n");
            
            if (divide == False):
                print(f"Coins = {player.coins}");
                print(f"Bet = {bet}\n");
                print(f"Cards leftover = {len(deck)}");
                print(f"Coins = {player.coins}");
                print(f"Left Bet = {left_bet}, Right Bet = {right_bet}");
                print_hand(table.cpu_hand, "CPUBot");
                print_hand(table.player_hand, "Player");
                result = bust(sum_of_hand(table.player_hand),
                              sum_of_hand(table.cpu_hand));
                player.payout(bet, result);
                player.write_results(file, bet, result);
            
            # deck was split
            else:
                print(f"Cards leftover: {len(deck)}");
                print_hand(table.cpu_hand, "CPUBot");
                print_hand(left, "Player-Left");
                print_hand(right, "Player-Right");
                result = bust(sum_of_hand(left),
                              sum_of_hand(table.cpu_hand));
                resultTwo = bust(sum_of_hand(right),
                                 sum_of_hand(table.cpu_hand));


                # deck was split and double-downed on left side
                if (left_dbl == True):
                    player.payout(left_bet, result);
                    player.write_results(file, left_bet, result);
                
                # deck was split and left side payout
                else:
                    player.payout(bet, result);
                    player.write_results(file, bet, result);
                
                # deck was split and double-downed on right side
                if (right_dbl == True):
                    player.payout(right_bet, resultTwo);
                    player.write_results(file, right_bet, result);
                
                # deck was split and right side payout
                else:
                    player.payout(bet, resultTwo);
                    player.write_results(file, bet, resultTwo);
                
                left.clear();
                right.clear();
            
            print(f"[SYSTEM]: Your new balance is {player.coins}!");
            file.write(f"Round concluded, Coins: {player.coins}\n\n");

            if (player.coins <= 0):
                file.write(f"Gain: {player.coins - start_amount}\n");
                sys.exit("\n[SYSTEM]: You have been kicked out of the "
                         "casino.\nReason: You ran out of money.");
            
            userInput = input("\n[SYSTEM]: Type quit or anything to "
                              "continue: ").strip().lower();
            table.flush();

        file.write(f"Gain: {player.coins - start_amount}\n");



# testing environment
def test_envir():
    ...



# main function
def main():
    game();



if __name__ == "__main__":
    main();