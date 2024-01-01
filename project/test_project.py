import pytest
import project

def test_sum_of_hand():
    empty_deck = [];
    size_one_deck = [("Hearts", 1)];
    small_deck = [("Hearts", 1), ("Diamonds", 5), ("Spades", 1)];

    assert project.sum_of_hand(empty_deck) == 0;
    assert project.sum_of_hand(size_one_deck) == 11;
    assert project.sum_of_hand(small_deck) == 17;