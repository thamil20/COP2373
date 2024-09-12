# This program accepts an email as a string of text and displays a
# "spam score" based on how many keywords or phrases are present.

# A function designed to return a list of spam flags and integer
# representing the spam score for a given email based on a predetermined
# list of spam flags.
def email_spam_score(flags:list, email:str)->(list, int):

    # A list to retain the counted spam flags to later display to the
    # terminal.
    counted_spam_flags = []

    # An integer to retain the amount of counted spam flags in a given
    # email.
    spam_score = 0

    # Iterate over each flag to check the email for every flag
    # independently.
    for flag in flags:

        # Check if the lowercase instance of the flag is within
        # the lowercase instance of the provided email.
        if flag.lower() in email.lower():

            # If the flag is in the email, add the flag to the end of
            # the list of counted spam flags.
            counted_spam_flags.append(flag)

            # If the flag is in the email, add one to the counter
            # variable.
            spam_score += 1

    # Join the counted spam flags together as a single string separated
    # by commas to later display to the terminal as a readable list
    # within a sentence.
    counted_spam_flags = ', '.join(counted_spam_flags)

    # Returns a tuple containing the score and list of counted flags.
    return counted_spam_flags, spam_score


# A function designed to run the functionality of the program
# when ran directly, prints to the terminal when called.
def main()->print:

    # A list of words or phrases that are known to be spam flags.
    spam_flags:list = ['Debt Relief', 'Instant Access', 'Pure Profit',
                       'Limited Time', 'Special Promotion',
                       'Lowest Price', 'Best Price', 'Credit Card',
                       'Dear Friend', 'ASAP', 'Madam', 'Free',
                       'Lower Interest Rates', 'Click Here',
                       'Own Boss', 'Join Millions', 'Extra Cash',
                       'No Hidden Fees', 'Financial Freedom', 'At Risk',
                       'Big Bucks', '$$$', 'Buy Direct', 'Call Free',
                       'Increase Sales', 'Credit Repair', 'Biz',
                       'New Customers Only', 'No Credit Check',
                       'Meet Singles']

    # Get an email to score from the user.
    user_entry = input('Please enter the text of an email in one line:\n')

    # Save the flags and score returned from the entered email as list
    # integer variables respectively.
    user_flags, user_score = email_spam_score(spam_flags, user_entry)

    # Display the percentage chance of the email being spam.
    print('\nThe percentage of found spam words was '
          f'{(user_score/len(spam_flags))* 100:.2f}%')

    # Display the user's spam score and flagged words or phrases in a
    # readable sentence.
    print(f'\nYour spam score is {user_score}/{len(spam_flags)} and the '
          f'words or phrases that were flagged are "{user_flags.lower()}"')

if __name__ == '__main__':
    main()