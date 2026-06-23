# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  One bug that I noticed was as mentioned which was that the hints that were given werent correlating with the expected output

  Another bug was when I was changing the mode to "Easy", the number I was supposed to guess was out of range. For example the number I had to guess was 95 but the range was from 1-20.

  Another bug was the mismatch of the number of guesses left and total attempts allowed. For example, in the normal mode, total attempts is 8 but it says 7 attempts left, even if i havent guess yet. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guessed 60 | "Go Higher" | "Said "Go Lower" | none |
| changed to 'Hard' | the range should much bigger from 1-100 | the range was 1-50 instead | none |
| click 'New Game' | restarts the game | restarts the attempts, but still has the message saying "Game over. Start a new game to try again." | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I asked Claude about the mismatch of attmepts left and total attempts. Claude gave a really detailed and clear explaination why attempts was 1 less, and it was because it was initialized incorrectly and calulated as "limit - attempt". 
I saw where the changed needed to happen as Claude highlighted it for me, and confirmed the changes.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

When I asked Claude about the return message saying "Go HIGHER" when the number is too high or vise versa, Claude said that its because "The secret gets cast to a string on even attempts which "forces a lexicographic (alphabetical) comparison instead of a numeric one."
I decided to check the code that actually compares the guess with the secret number, turns out it was just wrong message outputted. When i corrected Claude, it said "You're right — good catch, and I over-complicated it..."
I saw where the changed needed to happen as Claude highlighted it for me, and confirmed the changes.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I determined whether a bug was fixed with test cases that Claude generated. I also checked by running the app and checking the features myself if they did as intended 

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

One of the test that I ran was manually checking that the range of the chosen mode changes when the user selects easy, normal or hard. It showed me how the code was responding accurately with the users input.

- Did AI help you design or understand any tests? How?

Yes it did help me a lot. Starting off i didnt know where to look to understand the code and program and the bugs. But when I asked Claude to explain each function to me and it explained how they worked, easily helping me figure out the bugs in the functions.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
