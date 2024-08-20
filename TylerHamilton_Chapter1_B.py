# Tyler Hamilton Exercise 1B This program simulates the responses of a
# Magic 8 Ball.
# Import the random module to randomly choose a Magic 8 Ball response.
import random

# create_responses is a function designed to create a file containing a
# list of possible Magic 8 Ball responses.
def create_responses_file():

    # Create a new file to write the possible resposnes from a
    # Magic 8 Ball.
    with open('8ball_responses.txt', 'w') as file:

        # A list of responses to write to the file for the
        # program to use.
        magic_8_ball_responses = [
            "Yes, of course!\n",
            "Without a doubt, yes.\n",
            "You can count on it.\n",
            "For sure!\n",
            "Ask me later!\n",
            "I'm not sure.\n",
            "I can't tell you right now.\n",
            "I'll tell you after my nap.\n",
            "No way!\n",
            "I don't think so.\n",
            "Without a doubt, no.\n",
            "The answer is clearly NO!\n",
        ]

        # Write each element of the list magic_8_ball_resposnes to the
        # file to later read and use as output.
        file.writelines(magic_8_ball_responses)

# read_responses is a function designed to create a list by reading the
# lines of a file containing Magic 8 Ball responses.
def read_responses_file():
    # Call create_responses to create the file containing responses.
    create_responses_file()

    # Open the file to read the responses and choose one to output.
    with open('8ball_responses.txt', 'r') as file:

        # Create a list by reading the lines of the file into the list.
        magic_8_ball_responses = [line for line in file]

    # Return the list of responses as an object.
    return magic_8_ball_responses


# get_answers is a function designed to prompt a user to ask a yes or
# no question which will be answered by one of the responses within the
# list returned from read_responses.
def get_answers(magic_8_ball_responses=[]):

    # Create a variable to stop the loop when necessary.
    running = True

    # The program should continuously answer questions.
    while running:

        # Prompt the user for their question, also reminding them
        # how they are able to quit.
        user_question = input("Ask any yes or no type question "
                              "or type quit to quit: ")

        # Allow the user to quit.
        if user_question.lower() == "quit":

            # Stop the loop and quit the program.
            running = False

        # Check if the user typed anything, they need to ask a question.
        elif user_question.lower() == "":

            # Alert the user that they have not typed anything.
            print("Please input a question.\n")

        # If the user does not enter quit, the program runs.
        else:

            # Choose a random response to the question
            response = random.choice(magic_8_ball_responses)

            # Display the 8-ball's response to the user.
            print(response)

if __name__ == '__main__':
    get_answers(read_responses_file())