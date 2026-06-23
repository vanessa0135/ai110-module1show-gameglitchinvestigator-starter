from logic_utils import check_guess, parse_guess, get_range_for_difficulty

#----checks the validity of check_guess and its returned message
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, the outcome should be "Too High"
    # (this is the high/low bug we fixed: a higher guess must report "Too High")
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, the outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

#----checks validity of get_range_for_difficulty and parse_guess
def test_guess_out_of_range_above():
    # On Normal difficulty the valid range is 1..100.
    # A guess of 999 is OUTSIDE that range.
    low, high = get_range_for_difficulty("Normal")
    guess = 999
    # The guess is genuinely out of range
    assert not (low <= guess <= high)

    # Current behavior: the program does NOT reject out-of-range guesses.
    # parse_guess still accepts it as a valid number...
    ok, value, error = parse_guess(str(guess))
    assert ok is True
    assert value == 999
    assert error is None

    # ...and check_guess still compares it, reporting "Too High".
    outcome, message = check_guess(guess, 50)
    assert outcome == "Too High"

def test_guess_out_of_range_below():
    # A guess of -5 is below the valid range of 1..100 on Normal.
    low, high = get_range_for_difficulty("Normal")
    guess = -5
    assert not (low <= guess <= high)

    ok, value, error = parse_guess(str(guess))
    assert ok is True
    assert value == -5
    assert error is None

    outcome, message = check_guess(guess, 50)
    assert outcome == "Too Low"
