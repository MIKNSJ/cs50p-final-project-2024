# Modified Blackjack

This is a final project for the following course CS50P: Introduction to Python.

You can see a demo of this program [here](https://youtu.be/Y_E3LRr4nGs?si=dayE0Z54b4fA-fs0).

***

## Description of the Project

This project is about a table/card game that is regularly seen in casinos known as [Blackjack](https://en.wikipedia.org/wiki/Blackjack). In Blackjack, a player goes against the dealer, by betting money, in which for every card that is drawn, the total value of a hand should not exceed 21. Therefore, if this rule is satisfied with the player also having a hand with the higher sum then the dealer, then the player wins. In this game, there are basic moves of controlling a given hand that Blackjack offers to a player in order to beat the dealer. The basic moves are as follows: hit, stand, double down, and split. However, this project will feature a modified version of this game featuring three additional moves for the player which includes peek, swap, and special. These new moves, along with the basic moves, can be used against the dealer denoted as CPU (computer). The first move which is peek allows the player to look at the next card that will be drawn. Second, we have swap which allows the player to swap their hand with the computer. Lastly, calling special allows the player to draw one special card with a random negative value in the range -5 to -1. It is important to note that the moves, excluding hit/draw, can be only used once per turn and only the player itself. There is no drawback/penalty for using the new moves it is merely a player's choice. However, with high stakes can be involved, a player should aim to win by at all costs.

***

## Files of the Project

In this project, we have the following files: project.py, test_project.py, and log.txt.


### project.py

This is the main file which contains all the instructions to generate a working Blackjack game.


### test_project.py

This is a tester file for unit tests. We want to test individual functions, such as the moves that a player can make before combined them into a single moveset.


### log.txt

You may have an additional file generated after running the Blackjack program successfully that records the statistics of the current session. Such statistics may include: username, coins, bet amount, win/lose, payout, and net gain.


Note: If you run the python compile/run command instead of pytest on the file test_project.py, then you may have an additional folder/directory in project directory called __pycache__.

***

## Design/Implementation Analysis of the Project

In this project, basic Python topics/features are used in order to create this program.


### Data Structure

The focus on using lists as it can represent the idea of the cards contained in a player/computer's hand.


### Object-Oriented

The development of two classes: player and table. The player class serves to know the name of the current player and to keep track of the balance (coins) in real time after placing a bet and either winning, losing, or tying through the use of a player object. While the table class serves to create a hand represented as a list for the player and the computer to store cards through the use of a table object. In addition, the class comes with an method called flush() in which will clear (empty) the lists in order for the player and the computer to play again.


### File Output

A output file called log.txt is written on the statistics of the current session. Such statistics may include: username, coins, bet amount, win/lose, payout, and net gain.
This is helpful for a player to see win/lose streaks or just the history alone after the program as ended.


### Functions

This includes, but not all, various moves of a player are broken down into each individual function where calling the function corresponds to a player making that move.

***

## func.docs

In this project, we want to list the descriptions of some functions.


### split()

If we are given one list, and the first two cards have the same value, then we can split into two separate lists with one card in one list and vice versa.

*Note: For this version of Blackjack, this game allows at most one split to occur meaning that normal house rule of at most 3 nested splits cannot occur.*


### double_down()

The player agrees to double the current bet in which by receiving one more card and standing.


### game()

Still, a player can make other moves after splitting, so the use of boolean values can allow separate cases of when a player has only one or two hands. This is shown in the file in which we denote a variable called divide. If a player has two hands, then moves are chosen between the two hands. If one hand goes over a sum of 21, then the other hand can still make moves if under 22. In addition, a player can call double down on either one or both of the hands so boolean values has to be used again to separate the payout between hands with respect to the new bet value. This is shown in the file by using boolean values left_dbldown and right_dbldown.

***