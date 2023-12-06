import random
import time

# Define questions and answers for each level
levels = {
    1: {
        "questions": {
            "Real Name": {
                "question": "What is Cinderella's real name?",
                "options": ["Ella", "Cindy", "Anastasia"],
                "correct_answer": "Ella",
                "points": 2
            },
            "Fierey locks": {
                "question": "How many princesses have redhair?",
                "options": ["1", "2", "3"],
                "correct_answer": "2",
                "points": 2
            },
            "Papa Inventor": {
                "question": "Which princess had a father who was an inventor?",
                "options": ["Tiana", "Belle", "Merida"],
                "correct_answer": "Belle",
                "points": 2
            },
            "Ariel's treasure": {
                "question": "What is a dinglehopper in The Little Mermaid?",
                "options": ["Hair Brush", "Candlestick", "Fork"],
                "correct_answer": "Fork",
                "points": 2
            },
             "Slippery Slipper": {
                "question": "Which shoe did Cinderella leave behind at the ball?",
                "options": ["Right", "Left", "They didn't say"],
                "correct_answer": "Left",
                "points": 3
            },
            # Add more questions for level 1
        }
    },
    2: {
        "questions": {
            "Ariel": {
                "question": "Which sea creature is Ariel's best friend?",
                "options": ["Flounder", "Sebastian", "Scuttle"],
                "correct_answer": "Flounder",
                "points": 3
            },
            "Good morning": {
                "question": "Which princess' name means dawn?",
                "options": ["Rapunzel", "Tiana", "Aurora"],
                "correct_answer": "Aurora",
                "points": 3
            },
            "Mother Dear": {
                "question": "What is the name of Rapunzel's mother?",
                "options": ["Donna", "Gothel", "Drizella"],
                "correct_answer": "Gothel",
                "points": 3
            },
            "Who needs a dress": {
                "question": "Who was the first princess to wear pants?",
                "options": ["Merida", "Jasmine", "Mulan"],
                "correct_answer": "Jasmine",
                "points": 3
            },
            "Undercover Princess": {
                "question": "What name does Princess Aurora go by to protect her identity?",
                "options": ["Briar Rose", "Agath", "Anastasia"],
                "correct_answer": "Briar Rose",
                "points": 3
            },
            # Add more questions for level 2
        },
        "time_limit": 15  # Time limit for level 2 questions (in seconds)
    },
    3: {
        "questions": {
            "Belle": {
                "question": "What is the name of Belle's father?",
                "options": ["Maurice", "Gaston", "LeFou"],
                "correct_answer": "Maurice",
                "points": 4
            },
            "Gothel's many lives": {
                "question": "How old is Gothel (Rapunzel's Mother) at the time of the movie?",
                "options": ["90", "387", "290"],
                "correct_answer": "387",
                "points": 4
            },
            "Enchanted Cake": {
                "question": "Which animal does the enchanted cake turn Merida's mother into?",
                "options": ["Goat", "Wolf", "Bear"],
                "correct_answer": "Bear",
                "points": 4
            },
            "Genie in a bottle": {
                "question": "How  many years was the Genie stick in the lamp before Aladdin released him?",
                "options": ["100", "1000", "10000"],
                "correct_answer": "10000",
                "points": 4
            },
            "Snow White's Kiss": {
                "question": "What is the name of Snow White's prince?",
                "options": ["Prince Florian", "Prince Eugene", "Prince John"],
                "correct_answer": "Prince Florian",
                "points": 4
            },
            "RSVP to the Ball": {
                "question": "What time does the royal ball start in Cinderella?",
                "options": ["11 PM", "6 PM", "8 PM"],
                "correct_answer": "8 PM",
                "points": 4
            },
             "Bavarian": {
                "question": "Which princess lives in Bavaria?",
                "options": ["Aurora", "Snow White", "Cinderella"],
                "correct_answer": "Snow White",
                "points": 4
            },
             "Siblings": {
                "question": "Which princess has three brothers?",
                "options": ["Snow White", "Jasmine", "Merida"],
                "correct_answer": "Merida",
                "points": 4
            },
             "Friendly Nicknames": {
                "question": "Which nicknames do princess Tiana and Charlotte give each other?",
                "options": ["Char & Ana", "Char & Tia", "Lotte & Tia"],
                "correct_answer": "Lotte & Tia",
                "points": 4
            },
             "Breakfast is served!": {
                "question": "What did Mulan's friend, Mushu, make her for breakfast?",
                "options": ["Pancakes", "Porridge", "Mochi Rice"],
                "correct_answer": "Porridge",
                "points": 4
            },
             "Father's Approval": {
                "question": "Who does Pocahontas' father want her to marry?",
                "options": ["Kocoum", "Radcliffe", "John Smith"],
                "correct_answer": "Kocoum",
                "points": 4
            }, # End of Level 3 & Game
        },
        "time_limit": 10  # Time limit for level 3 questions (in seconds)
    }
}

# Function to ask questions with time limit
def ask_question_with_time_limit(princess, question_data, level):
    print(f"\n{princess} Trivia:")
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

    start_time = time.time()
    user_answer = input("Enter the number of your answer: ")
    elapsed_time = time.time() - start_time

    if level > 1 and elapsed_time > levels[level]["time_limit"]:
        print(f"Time's up! The correct answer is {question_data['correct_answer']}.")
        return None

    return question_data["options"][int(user_answer) - 1]

# Function to play the whole game
def play_game():
    print("Welcome to the Disney Princess Trivia! The questions are based on the 11 original Disney Princeses")
    print("The original 11 are Merida, Ariel, Mulan, Pocahontas, Belle, Snow White, Tiana, Cinderella, Aurora, Jasmine, and Rapunzel.")
    print("Let's begin!")
    user_name = input("Enter your name: ")
    user_scores = {"name": user_name, "score": 0, "level": 1}

    for level in range(1, 4):
        questions = levels[level]["questions"]
        score_per_level = sum(question["points"] for question in questions.values())

        print(f"\nLevel up! Welcome to Level {level}!")
        score = 0

        for princess, question_data in questions.items():
            user_choice = ask_question_with_time_limit(princess, question_data, level)

            if user_choice == question_data["correct_answer"]:
                print(f"Correct! You earned {question_data['points']} points.\n")
                score += question_data["points"]
            else:
                print(f"You guessed wrong, the correct answer is {question_data['correct_answer']}.\n")

        level_passed = score >= 0.7 * score_per_level
        user_scores["score"] += score
        user_scores["level"] = level

        if not level_passed:
            print(f"Oops! You didn't pass Level {level}. Get the popcorn out and keep studying. Here's a suggestion for a movie to watch: Rapuzel, Mulan, and Sleeping Beauty!\n")
            break

        print(f"Congratulations! You passed Level {level}. Your current score is {user_scores['score']}.\n")

    print(f"Your final score is {user_scores['score']} and you reached Level {user_scores['level']}.")

    # Add user to the leaderboard
    update_leaderboard(user_scores)

# Function to update the leaderboard
def update_leaderboard(user_scores):
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = eval(file.read())
    except (FileNotFoundError, SyntaxError):
        leaderboard = []

    leaderboard.append(user_scores)

    # Sort the leaderboard based on scores (descending order)
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)

    # Save the updated leaderboard back to the file
    with open("leaderboard.txt", "w") as file:
        file.write(str(leaderboard))

    # Display leaderboard
    display_leaderboard(leaderboard)

# Function to display the leaderboard
def display_leaderboard(leaderboard):
    print("\nLeaderboard:")
    for i, entry in enumerate(leaderboard, start=1):
        print(f"{i}. {entry['name']} - Score: {entry['score']}, Level: {entry['level']}")

# Function to ask if the user wants to play again
def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

# Main loop
while True:
    play_game()

    if not play_again():
        print("Thanks for playing! Bye!")
        break
