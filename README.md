# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
A number guessing game wher the user has limit guess attempts, and a secret number that they must find. It is a quick and easy game that anyone can enjoy!

- [X] Detail which bugs you found.

1. One bug that I noticed was that the hints that were given werent correlating with the expected output

2. Another bug was when I was changing the mode to "Easy", the number I was supposed to guess was out of range. For example the number I had to guess was 95 but the range was from 1-20.

3. Another bug was the mismatch of the number of guesses left and total attempts allowed. For example, in the normal mode, total attempts is 8 but it says 7 attempts left, even if i havent guess yet. 

- [X] Explain what fixes you applied.

1. Changed the return messages in check_guess so that its correct

2. Changed the values in get_range_for_difficulty

3. Used Claude to help me fix calculation and initialization errors

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters 50
2. Returned message says "Go LOWER!"
3. User then enters 25 -> "Go LOWER!"
4. User then enters 15 -> "Go LOWER!"
5. User then enters 10 -> "Go LOWER!"
6. User then enters 5 -> "Go HIGHER!"
7. User then enters 8 -> "Go HIGHER!"
8. User then enters 9 -> "Correct!" -> Game ends
9. User guesses correctly and new game automatically starts when you input new number


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ===================================================================== 5 passed in 0.02s =====================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
