#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import find_first_ranked_word, NotEnoughValues

def testFindFirstRankedWord():

    ### Nominal Cases
    assert find_first_ranked_word(["bob", "alice", "eve"]) == "alice"
    assert find_first_ranked_word(["alice", "bob"]) == "alice"
    assert find_first_ranked_word(["a", "ab", "aa"]) == "a"
    assert find_first_ranked_word(["zeta", "alpha", "alpha"]) == "alpha"
    assert find_first_ranked_word(["banana", "apple", "cherry", "apple"]) == "apple"
    ###

    ### Edge cases and corner cases
    assert find_first_ranked_word(["Ant", "ant", "Bee"]) == "Ant"
    assert find_first_ranked_word(["mango", "Mango"]) == "mango"
    assert find_first_ranked_word(["b", "a"]) == "a"
    with pytest.raises(NotEnoughValues):
        find_first_ranked_word(["alone"])

    with pytest.raises(NotEnoughValues):
        find_first_ranked_word([])
    
