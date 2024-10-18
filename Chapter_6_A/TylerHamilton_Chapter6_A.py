# Create functions to validate phone numbers, social security numbers and zip codes using regular expressions. 
# Create a main function to get input from a user and then displaying if the phone number, social security number and zip code they entered is valid. 
import re

def phone_validation(phone_number):
    if re.match(r'^\d{3}-\d{3}-\d{4}$', phone_number):
        return True
    elif re.match(r'^\d{10}$', phone_number):
        return True
    else:
        return False

def social_validation(social_number):
    if re.match(r'^\d{3}-\d{2}-\d{4}$', social_number):
        return True
    elif re.match(r'^\d{9}$', social_number):
        return True
    else:
        return False

def zip_validation(zip_code):
    if re.match(r'^\d{5}-\d{4}$', zip_code):
        return True
    elif re.match(r'^\d{5}$', zip_code):
        return True
    else:
        return False

def main():
    phone_number, social_number, zip_code = [input("Please enter a phone number: "),
                                             input("Please enter a social security number: "),
                                             input("Please enter a zip code: ")]
    phone_val = phone_validation(phone_number)
    social_val = social_validation(social_number)
    zip_val = zip_validation(zip_code)
    if phone_val & social_val & zip_val == True:
        print("Phone number, social security number, and zip code are all valid.")
    elif phone_val & social_val == True:
        print("Phone number and social security number are valid.")
    elif zip_val & social_val == True:
        print("Zip code and social security number are valid.")
    elif phone_val & zip_val == True:
        print("Phone number and zip code are valid.")
    else:
        print("None of the entered values are valid, please try again.")

main()
