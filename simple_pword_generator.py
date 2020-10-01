def pword_gen():
    
    from secrets import randbelow
    import string
    #setting up a list of possible symbols for the password
    pword_symbols_list = string.ascii_letters+string.digits+string.punctuation
    pword = ''
    
    while True:
        pword_length = input("How many characters do you want this password to be?")
        
        try: 
            pword_length = int(pword_length)
            
            if pword_length <= 0: #if the input is not a positive integer, retry
                print("Sorry, input must be positive and non-zero.")
                continue
            else:
                break
                
        except ValueError: #if the input is not a number, retry
            print("Input a positive integer, please.")
            continue
    
    for i in range(pword_length):
        pword += pword_symbols_list[randbelow(94)]
        
    print(f"Your new password is:\n{pword}")
    if input("Do you want this copying to your clipboard? Press y for yes.").lower() == "y":
        pyperclip.copy(pword)
    print("Keep it safe!")


pword_gen()