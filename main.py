import random


class HitAndBlowGame:
    def __init__(self):
        # Initialize the game attributes: answer, guess, and digit count.
        self.answer = []
        self.guess = []
        self.digit = 0

    def generate_random_answer(self):
        """
        Generate a random answer based on the user's input for the number of digits.
        The first digit cannot be zero to ensure valid formatting.
        """
        while True:
            # Ask the user to input the number of digits for the game (between 3 and 9).
            _digit = input("Input a number of digits (between 3 and 9): ")
            if _digit.isdigit() and 3 <= int(_digit) <= 9:
                self.digit = int(_digit)
                break
            else:
                print("Please enter a valid number between 3 and 9.")

        # Generate the random answer: the first digit is 1-9, the rest can be 0-9.
        self.answer = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(self.digit - 1)]
        print("Answer has been set. Start guessing!")  # Debugging tip: print(f"Answer: {self.answer}")

    def get_player_guess(self):
        """
        Get the player's guess, ensuring it matches the required number of digits.
        The guess must be numeric and have the exact length specified by the game.
        """
        while True:
            # Ask the player to input their guess.
            guess = input(f'Guess a number with {self.digit} digits: ')
            if guess.isdigit() and len(guess) == self.digit:
                # Convert the input string into a list of integers.
                self.guess = [int(x) for x in list(guess)]
                break
            else:
                print(f"Guess must be a number with exactly {self.digit} digits.")

    def evaluate_guess(self):
        """
        Compare the player's guess to the answer and calculate the number of Hits and Blows.
        Returns True if the game should continue, or False if the player has won.
        """
        hit = 0
        blow = 0
        remaining_guess = []
        remaining_answer = []

        # Check for Blows: exact matches in both digit and position.
        for i in range(len(self.guess)):
            if self.guess[i] == self.answer[i]:
                blow += 1
            else:
                # Collect digits that do not match for further comparison in the Hit check.
                remaining_guess.append(self.guess[i])
                remaining_answer.append(self.answer[i])

        # Check for Hits: matching digits in the wrong positions.
        for g in remaining_guess:
            if g in remaining_answer:
                hit += 1
                # Remove the matched digit from the answer to avoid duplicate counting.
                remaining_answer.remove(g)

        # Display the results of this round.
        print(f'Hit: {hit}  Blow: {blow}')

        # Return False if all digits are Blows (player wins), otherwise True.
        return blow != self.digit

    def start_game(self):
        """
        Start the Hit and Blow game, controlling the flow of setting the answer,
        fetching guesses, and evaluating guesses until the player wins.
        """
        # Generate the random answer.
        self.generate_random_answer()

        is_playing = True
        while is_playing:
            # Fetch the player's guess and evaluate it.
            self.get_player_guess()
            is_playing = self.evaluate_guess()

        # End the game with a winning message.
        print("You Won!")


if __name__ == "__main__":
    # Entry point for the game. Create an instance of the GamePreparation class and start the game.
    game = GamePreparation()
    game.start_game()
