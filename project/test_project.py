import pytest
import project



empty_deck = [];
size_one_deck = [("Hearts", 1)];
small_deck = [("Hearts", 1), ("Diamonds", 5), ("Spades", 1)];
a_deck = [("Alpha", 101)];
b_deck = [("Beta", 905)];



def test_sum_of_hand():
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



def test_peek():
    assert project.peek(empty_deck) == "exit";
    assert project.peek(size_one_deck) == ("Hearts", 1);
    assert project.peek(small_deck) == ("Hearts", 1);



def test_swap():
    new_a_deck, new_b_deck = project.swap(a_deck, b_deck);

    assert new_a_deck == b_deck;
    assert new_b_deck == a_deck;



def test_special_cards():
    new_empty_deck = project.special_cards(empty_deck.copy());
    new_size_one_deck = project.special_cards(size_one_deck.copy());
    new_small_deck = project.special_cards(small_deck.copy());

    assert len(new_empty_deck) == 1;
    assert len(new_size_one_deck) == 2;
    assert len(new_small_deck) == 4;
    assert project.sum_of_hand(new_empty_deck) < 0;
    assert project.sum_of_hand(new_size_one_deck) < 11;
    assert project.sum_of_hand(new_empty_deck) < 17;
    assert project.special_cards(new_small_deck) == "exit";



def test_draw():
    new_size_one_deck, draw_card = project.draw(size_one_deck.copy());

    assert project.draw(empty_deck.copy()) == "exit";
    assert len(new_size_one_deck) == 0;
    assert draw_card == ("Hearts", 1);