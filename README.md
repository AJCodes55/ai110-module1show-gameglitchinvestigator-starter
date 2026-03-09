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


- The games purpose was to guess the secret key in 7 attempts. if the guess if lower than the secret key, the UI should prompt 'Go HIGHER' else' go LOWER'. if the guess is correct in 7 attempts, we have won the game
- I found 3 bugs in the game
 1) THe 'New game' button was not workig properly. Ideally it should reset the total attempts, secret, and score, but it does ot reset the score.

  2) 'Enter your guess' accepts zero and negative numbers as well. Also it accepts numbers which are not in the range of 1-100. Ideally it should only accept numbers from 1-100

  3) The logic for guessing the correct secret is incorrect. When the guess is less than the secret - it tells us to go lower. and when the guess in more than the secret - it tells us to go higher. 

- For bug 1, the new_game function did not incorporate session_state for score, which was fixed once I added that
- for Bug 2, the range limitation was implemented which now only accepts number from 1-100
- for bug 3 , check_guess function was changed and refactored to logic_utils


## 📸 Demo

<img width="1019" height="816" alt="image" src="https://github.com/user-attachments/assets/6335512a-1e9b-4985-89bd-468a6933a6da" />


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
![alt text](<Screenshot 2026-03-09 at 4.39.54 PM.png>)
