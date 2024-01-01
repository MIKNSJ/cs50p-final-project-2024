import pytest
import project



def test_sum_of_hand():
    empty_deck = [];
    size_one_deck = [("Hearts", 1)];
    small_deck = [("Hearts", 1), ("Diamonds", 5), ("Spades", 1)];

    assert project.sum_of_hand(empty_deck) == 0;
    assert project.sum_of_hand(size_one_deck) == 11;
    assert project.sum_of_hand(small_deck) == 17;



def test_bust():
    # cpu wins
    player_one = 1;
    cpu_one = 2;

    # player wins
    player_two = 2;
    cpu_two = 1;

    # cpu wins
    player_three = 25;
    cpu_three = 13;

    # neither wins
    player_four = 21;
    cpu_four = 21;

    # player wins
    player_five = 5;
    cpu_five = 22;

    # player wins
    player_six = 21;
    cpu_six = 20;

    # cpu wins
    player_seven = 20;
    cpu_seven = 21;

    assert project.bust(player_one, cpu_one) == "cpu";
    assert project.bust(player_two, cpu_two) == "player";
    assert project.bust(player_three, cpu_three) == "cpu";
    assert project.bust(player_four, cpu_four) == "neither";
    assert project.bust(player_five, cpu_five) == "player";
    assert project.bust(player_six, cpu_six) == "player";
    assert project.bust(player_seven, cpu_seven) == "cpu";