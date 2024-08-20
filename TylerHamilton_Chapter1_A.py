# Tyler Hamilton Exercise 1A This program sells a set amount of pre-sale
# cinema tickets.

# A constant variable used to change the amount of available tickets
# that are available on the pre-sale.
AVAILABLE_TICKETS = 20

# ticket_pre_sale is a function that greets a user and loops to sell
# a limited number of pre-sale tickets for a cinema release.
def ticket_pre_sale(tickets_available=0):

    # Initialize a variable to hold the number of tickets left over/
    remaining_tickets = tickets_available

    # Initialize a variable to increment how many people bought tickets.
    num_buyers = 0

    # Print to the terminal to greet the user.
    print("Hello, today we are offering a pre-sale of "
          f"{remaining_tickets} cinema tickets. "
          "Each person may purchase up to 4 tickets.")

    # Looping through pre-sale ticket purchases until there are zero
    # tickets left to sell, returning a print statement to show how
    # many people purchased tickets.
    while remaining_tickets > 0:

        # Initialize a variable to store user input representing how
        # many tickets they wish to buy.
        num_tickets = int(input("Please enter the number of pre-sale "
                                "tickets you wish to buy (1-4): "))

        # People may only buy 1-4 tickets per purchase per person.
        if 0 < num_tickets < 5:

            # Subtract the amount of purchased tickets from the amount
            # of remaining tickets.
            remaining_tickets -= num_tickets

            # The cinema cannot sell more than 20 tickets, this checks
            # to ensure that remaining_tickets is never less than zero.
            if remaining_tickets < 0:

                # If remaining tickets is less than zero, this will
                # increase remaining_tickets to its previous value.
                remaining_tickets += num_tickets

                # This is printed to tell the user why their purchase
                # was not counted.
                print("We can only sell 20 tickets today, there is/are"
                      f" only {remaining_tickets} ticket(s) remaining.")

            # This is used to increment num_buyers up by one per
            # purchase when remaining_tickets is greater than zero.
            else:
                num_buyers += 1

        else:
            # This is printed to tell the user they are only able to buy
            # able to purchase 1-4 tickets.
            print("Sorry, we can only sell 1-4 tickets per person!")

        # This is printed to ensure the amount of remaining tickets is
        # shown after each purchase.
        print(f"There is/are {remaining_tickets} ticket(s) remaining.")

    # Returns a print statement to ensure the number of buyers is
    # printed to the terminal at the end of the loop.
    print(f"{num_buyers} people bought tickets.")


if __name__ == "__main__":
    ticket_pre_sale(AVAILABLE_TICKETS)