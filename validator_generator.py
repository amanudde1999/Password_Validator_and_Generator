
def validate(password): 
# All characters are placed into different lists    
    special = ['!','#','$','%',"'",'*','(',')','*','+','.','/',':',';','?','>','<','=','?','@','[]','^','{','}','~']
    numbers = '1234567890'
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrsturvwxyz'
# Variables that will be used as flags in the while loops are initialized    
    secure_special,secure_number,secure_capital,secure_lower = (0,0,0,0)
# Counts are initialized    
    i,j,l,m = (0,0,0,0)
# Variables that will store the values 1 or 0 if they are true or false respectively.
    invalid,insecure,secure  = (0,0,0)
    result = ' '
# For loop to detect invalidity 
    for elements in range(len(password)):
        if len(password) < 8 or password.isspace() == True or password[elements] == '_' or password[elements] == '-' or password[elements] == ' ':
            invalid = 1

        else:
# First while loop checks for special characters. 
            while secure_special == 0 and i < len(password):
                if password[i] in special: 
# secure_special is set to 1 (True) if there is a special character.
                    secure_special = 1
                else: 
                    i += 1
# Second while loop checks for numbers
            while secure_number == 0 and j < len(password):
                if password[j] in numbers:
# secure_number is set to 1 (True) if there is a number.                    
                    secure_number = 1
                else:
                    j += 1
# Third while loop checks for capital letters.
            while secure_capital == 0 and l < len(password):
                if password[l] in capital:
# secure_capital is set to 1 (True) if there is a capital letter.  
                    secure_capital = 1
                else:
                    l += 1 
# Fourth while loop checks for lower case letters.
            while secure_lower == 0 and m < len(password):
                if password[m] in lower:
# secure_lower is set to 1 (True) if there is a lowercase letter.  
                    secure_lower = 1
                else: 
                    m += 1
# If statement to see if all conditions are satisfied for security if not, then insecure
            if secure_special == 1 and secure_capital == 1 and secure_number == 1 and secure_lower == 1:
                secure  = 1
            elif secure_special != 1 or secure_capital != 1 or secure_number or 1 or secure_lower != 1:
                insecure = 1
# Result is stored based on the satisfaction of the previous conditions
    if invalid == 1:
        result = 'Invalid'
    elif insecure == 1:
        result = 'Insecure'
    elif secure  == 1:
        result = 'Secure'
# The final result is outputted
    return result

    

def generate(n):
# Random module is imported.  
    import random 
# Password is stored as an empty string.   
    password = ''
# All possible characters are stored onto one variable as a type str
    options = "!#$%&'()*+,./:;<=>?@[]^`{|}~ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
# The flag variable is initialized (to be used in while loop)    
    safe = 0
# While loop that continues to generate passwords until secure.
    while safe == 0:
# For loop that generates the password.
        for i in range(n):
            password += random.choice(options)
# Validate function is used to guarantee security.
        if validate(password) == 'Secure':
            safe = 1
        else:
            safe = 0
            password = ''
# Generated password is outputted.
    return password

if __name__ == "__main__":

    password = input('Enter the password: ')
    print(validate(password))
    n = int(input('Enter the password character length: '))
    print(generate(n))

    

