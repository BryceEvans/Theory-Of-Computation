import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex



while line != "exit":
    # TODO Find matches

    
    # TODO If no match found, print that no number was found
    phone_num = r"([0-9]{10}|[0-9]{3}[-][0-9]{3}[-][0-9]{4}|[(][0-9]{3}[)]\s[0-9]{3}[-][0-9]{4}|[0-9]{3}\s[0-9]{3}\s[0-9]{4})"
    
    
    # TODO Else, break number up into area code, prefix, and suffic
    if re.findall(phone_num, line):
        num = ''.join(e for e in line if e.isalnum())
        area = num[:3]
        prefix = num[3:6]
        suffix = num[6:]
        print('Area Code: ', area, '\nPrefix: ', prefix, '\nSuffix: ', suffix)
    else:
        print('No number was found')

    
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!
    
    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")