# This program accepts a list of monthly expenses and display the total
# expense, highest expense, and lowest expense.
from functools import reduce

# gather_expenses gets individual expense types and amounts from the 
# user, separated by a comma. Then stores them in lists and uses those 
# lists to create and return a dictionary.
def gather_expenses() -> dict:

    # Initalize lists to hold expense types and amounts.
    type_list = []
    amount_list = []
    

    count = 0
    
    # Begin while loop to get multiple instances of user_expense and 
    # append each instance to a list.
    while True:
    
        # Try to get user input, strip it of whitespace, and split it
        # at the comma
        try:
            
            user_expense = input('Please enter the type of expense '
                                 'followed by the expense amount, '
                                 'separated by a comma and space. '
                                 '(Type "quit" when finished.)')
            
            expense_type, expense_amount = user_expense.strip().split(", ")
            
        # Break if user wishes to quit entering expenses, inform the 
        # user of the required format if they are attempting to input  
        # an expense in the wrong format.
        except:
            
            if user_expense.lower() == "quit":
                break
            
            print("Please use the following format: {type}, {amount}")
            
        else:
            # Check if the type is not in the list of types and add the 
            # type and amount to their respective lists.
            if expense_type not in type_list:
                
                type_list.append(expense_type)
                
                amount_list.append(int(expense_amount))
        

            else:
                # Initialize a counter variable to later count the 
                # indexes of the types list.
                count = 0
                
                # Iterate over the type list to find the index of the 
                # existing expense_type.
                for i in type_list:
                
                    # Check each index of type_list to see if it is the 
                    # same as the give expense_type.
                    if expense_type == type_list[count]:
                        
                        # Once the index is found, add the given 
                        # expense_amount to the current amount in that 
                        # index.
                        amount_list[count] += int(expense_amount)
                
                    # Increase count to ensure the entire list is 
                    # accounted for
                    count += 1

    # Create a dictionary of expenses using the type_list as keys 
    # and the amount_list as values.          
    expense_dict = {type:amount for (type,amount) in zip(type_list, 
                                                         amount_list)}
    
    return expense_dict



def main():
    
    # Gather the user's expenses using gather_expenses, returning a 
    # dictionary.
    expense_dict = gather_expenses()
    
    # Use the reduce function with a lambda returning the key:value pair
    # as a list of two elements as x if x is the highest value within 
    # the values of the dictionary, and returning them as y if y is
    # greater.
    highest_expense = reduce(lambda x, y: x if x[1] > y[1] else y, 
                             expense_dict.items())
    
    # Display the formatted results of highest_expense.
    print(f'Your highest expense for the month was {highest_expense[0]}, '
          f'and it costed you ${highest_expense[1]}.')
    
    # Use the reduce function with a lambda returning the key:value pair
    # as a list of two elements as x if x is the lowest value within 
    # the values of the dictionary, and returning them as y if y is
    # lower.
    lowest_expense = reduce(lambda x, y: x if x[1] < y[1] else y, 
                            expense_dict.items())
    
    # Display the formatted results of lowest_response.
    print(f'Your lowest expense for the month was {lowest_expense[0]}, '
          f'and it costed you ${lowest_expense[1]}.')
    
    
    total_expense = reduce(lambda x, y: x + y, expense_dict.values())
    
    # Use the reduce function with a lambda returning the accumulated
    # addition of each value in the dictionary.
    print('The total of all of your expenses for the month was '
          f'${total_expense}.')


if __name__ == "__main__":
    main()