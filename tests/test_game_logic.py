from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for Bug 2: input validation ---

def test_guess_zero_is_invalid():
    # Bug fix: 0 was previously accepted; should be rejected as out of range
    outcome, _ = check_guess(0, 50)
    assert outcome == "Invalid"

def test_guess_negative_is_invalid():
    # Bug fix: negative numbers were previously accepted; should be rejected
    outcome, _ = check_guess(-5, 50)
    assert outcome == "Invalid"

def test_guess_above_100_is_invalid():
    # Bug fix: numbers > 100 were previously accepted; should be rejected
    outcome, _ = check_guess(101, 50)
    assert outcome == "Invalid"

def test_guess_boundary_1_is_valid():
    # Lower boundary 1 must be accepted (not treated as invalid)
    outcome, _ = check_guess(1, 50)
    assert outcome != "Invalid"

def test_guess_boundary_100_is_valid():
    # Upper boundary 100 must be accepted (not treated as invalid)
    outcome, _ = check_guess(100, 50)
    assert outcome != "Invalid"


# --- Regression tests for Bug 3: hint direction was swapped ---

def test_hint_direction_guess_too_low():
    # Bug fix: when guess < secret the hint was incorrectly "go lower"
    # Correct behaviour: outcome should be "Too Low" (player needs to go higher)
    outcome, _ = check_guess(30, 70)
    assert outcome == "Too Low"

def test_hint_direction_guess_too_high():
    # Bug fix: when guess > secret the hint was incorrectly "go higher"
    # Correct behaviour: outcome should be "Too High" (player needs to go lower)
    outcome, _ = check_guess(80, 40)
    assert outcome == "Too High"

def test_hint_direction_not_swapped_low():
    # Extra guard: a low guess must never come back as "Too High"
    outcome, _ = check_guess(10, 90)
    assert outcome != "Too High"

def test_hint_direction_not_swapped_high():
    # Extra guard: a high guess must never come back as "Too Low"
    outcome, _ = check_guess(90, 10)
    assert outcome != "Too Low"
