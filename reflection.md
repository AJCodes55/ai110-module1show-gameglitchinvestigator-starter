# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  --> BUGS:
  When I ran the code, I saw multiple bugs

  1) THe 'New game' button was not workig properly. Ideally it should reset the total attempts, secret, and score, but it does ot reset the score.

  2) 'Enter your guess' accepts zero and negative numbers as well. Also it accepts numbers which are not in the range of 1-100. Ideally it should only accept numbers from 1-100

  3) The logic for guessing the correct secret is incorrect. When the guess is less than the secret - it tells us to go lower. and when the guess in more than the secret - it tells us to go higher. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
--> As a teammate , we used claude code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
--> the new game logic in the app.py file was breaking the new-game button. The AI Suggestted that it was not resetting the score. This was a good sugegstion.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
--> for the core logic of the game (bug 3), the AI suggested that 'parse_function' needs to be updated with a correct peice of code. However, when I navigated through the codebase, the issue was happening in a different function - check_guess
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
--> I applied the fix and tested it again
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  --> Th ebug was that it was accepting numbers which are not in teh range of 1 to 100. After applying the fix, i tested again by guessing negative numbers and positive numbers which are greateer than 100.
- Did AI help you design or understand any tests? How?
--> yes, AI helped my understand the test cases. I asked it to generate the test cases based on the bugs that i found and also asked it to explain the purpose of each test case 
--
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
--> In the original app, the secret number kept changing because of session_state. whenever a user pressed the new game button, the secret was changed to a random number between  1 to 100. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--> rerun is basically when the entire pyton script runs again from top to bottom. Whenever the reruns happen, the session_state would give you a feature of persistent memory that survies across reruns
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

--> I learned the debuging strategy and also refactoring logic into logic_utils.py. I will implement this into my future projects
- What is one thing you would do differently next time you work with AI on a coding task?
--> Not asking AI to "FIX THIS" , but rather understand the underlying issue with the help of AI .

- In one or two sentences, describe how this project changed the way you think about AI generated code.
--> The way i used to debug is quite different from what i have learnt in this project. This debugging methos is better as it helps to understand the core logic and how one piece of code is connected with other.