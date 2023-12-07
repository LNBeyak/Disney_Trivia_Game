# Disney_Princess_Trivia_Game

Disney Princess Trivia Game 

Welcome to the Disney Princess Trivia Game, a Python-based interactive quiz to test your knowledge of the 11 original princesses. This project was inspired by my four-year-old daughter, who has been quizzing me about princesses and filling our lives with crowns, dress up dresses, and courageous princess acts. The game is designed to provide an entertaining and educational experience for users who love Disney and want to challenge their understanding of the iconic characters. 

TABLE OF CONTENTS

	Introduction
	Features
	How to Play
	Levels
	Scoring
	Leaderboard
	Time Limit
	Design and Implementation
	Conclusions

INTRODUCTION

The Disney Princess Trivia Game is an interactive project that engages users with multiple-choice questions related to the eleven original Disney princesses. Player progress through three different levels, accumulate points, beat the timer, and challenge themselves with increasing difficulty. 

FEATURES

Features include:

-	Multiple levels of difficulty.
-	Users must score 70% or higher to move onto the next level.
-	Time limits for added challenge starting at Level 2.
-	A leaderboard to track progress and track users total scores.

HOW TO PLAY

1.	Introduction to the game followed by “Enter your name:” to provide your name to personalize your gaming experience. 
2.	Answer questions based on multiple-choice selection. 
3.	Accumulate points for correct answers to move on to the next level. 
4.	Progress through the levels by achieving a score of 70% or higher and beat the timer that begins in level 2.

LEVELS

The game has three levels, each with increasing difficulty. Users must successfully pass each level to unlock the next. Level 1 and Level 2 both have 5 questions. Level 3 has 10 questions. 

SCORING

Points are awarded for each correct answer which determines a passing score or not. Each level has a different number of points per correct answer. 
  o	Level 1 = 2 points per correct answer
  o	Level 2 = 3 points per correct answer
  o	Level 3 = 4 points per correct answer

Users must have a passing score to move up to the higher levels. If they do not pass with 70% (per level) or higher, they are given suggestions on what Disney movies to study. The total game points are accumulated and added to the leaderboard. 

LEADERBOARD

The leaderboard was added so players can compete with themselves or other players and see how their scores compare. The leaderboard is updated and displayed at the of each game. On the back end, the leaderboard keeps totals in a new *.txt file titled “leaderboard.txt”, created in the same working folder as the game file. Users are asked to play the game again after the leaderboard is displayed. 

TIME LIMIT

Starting on Level 2, a time limit is implemented. Users must answer within the specified time to earn points. Below are details of the time limits per level:
  o	Level 1: No Time Limit
  o	Level 2: 15 Seconds per question
  o	Level 3: 10 Seconds per question
If the user doesn’t answer within the time limits, they are notified that “Time’s Up!” and not given any points for that question. Users can still move on to the next question if they miss the time allotted.

DESIGN AND IMPLEMENTATION

To code the design of this project, I had to first research questions about Disney Princesses and find questions to ask. I organized them by difficulty to enter the ascending levels of difficulty. 

The following is a breakdown of how I organized my code to match the design features:

Levels, Questions, Scoring and Time Limit: Introduce the game, then insert questions based on their levels so they’re organized by data structure in a nested dictionary. This dictionary includes the scoring system where I assigned points to each question individually. 
The time limit is inserted at the end of each level.

Game Play, Time Limit, Leaderboard, and Main Loop: Coding the game to play using the questions created previously, I used a loop with function calls and user interaction. The ‘play_game()’ function is the main game loop. It starts with the introduction to the game and asks the user to enter their name. It moves through levels, asks questions, updates scores, and checks for progression. The function calls to complete these as well as displays results and includes user interaction decisions. 

Similarly, a loop function closer to the end of the code asks if the player wants to play again. This loop is the ‘play_again()’ function. 

Time Limit: The code function (‘ask_question_with_time_limit’) for the time limit has conditional statements, input handling, and time measurement to check for the elapsed time for each question to decide whether the user has answered within the allotted time. A ‘time’ module was added to measure the seconds allowed. 

Leaderboard: The function for the leaderboard (‘update_leaderboard()’)updates needed to sort a list and the creation of an external file I/O to track the players and their scores that can be updated as the game is played by different users. Each time the game is completed, the file is updated. 

Main Loop: Finally, the code concludes with a loop function that requires user interaction to call ‘play_game()’ and ‘play_again()’. It is the overall control structure that keeps the game running. 
In summary, as the game was being structured, I had to keep in mind the order of operations for each loop and their function. Initially, I had the time limit loop after the ‘game_play’ function and the timer wasn’t running. This was one of many lessons I learned during the project. 

CONCLUSIONS

My intention with this project was initially to create a simple game that could be executed easily. I started out with the basic setup and as I began to test it, I wanted to add more features. My intentions changed from just simply creating a workable code to adding value to the user’s experience, so it was fun and engaging. I wanted it to be challenging enough for users to want to compete and improve their knowledge to become better players. I learned that in game creation, it is important to keep the user’s experience in mind while designing the structure of the code. 

The more features, I wanted to implement, the more I learned about how to make the functions work together. As mentioned, I wanted to enhance the time limit loop function. I even attempted to adding a live timer that would warn players when the timer began and when they had 5 seconds left. I couldn’t get it to run properly and ultimately left it out. This could be considered a design flaw since the player doesn’t initially know how much time they must complete each question in Level 2 and 3 until they answer the question. They’re also not notified that they didn’t earn any points. 

Some features I am proud of are the leaderboard, and the advancement of levels. I think tracking results from each game helps the user to continue attempting the game again and again. The advancement of levels and their difficulty adds some pressure for the player to complete the game quickly and I was hoping it would limit them from doing an online search in between questions to find the answers if they didn’t know them already. 

Features I would like to add in the future include adding randomization to the questions and their answers so that the user was less likely to memorize the answers the more they played them. Creating a database with more questions that randomly play each time a player attempts the game would’ve been ideal. I would like to have also added a total time completed timer that is added to the leaderboard so players could compete for time. 

Initially, I had 10 questions per level, which made the game quite lengthy and I didn’t want users to lose interest in the beginning. I decided to add only 5 questions for the first two levels and then made the final level 10 questions. I’d like to add many more levels for players to progress through so there is more investment into the game and the ability to improve. 

Overall, I enjoyed building this project and had fun learning about princesses and what we learned in this course. I would like to continue advancing my skills with what we learned and get feedback to code this game more efficiently going forward. I believe there was a lot more I could have implement than just using loops and functions to make the experience for the user more exciting and advanced. I hope to improve on this during my coding journey. 
