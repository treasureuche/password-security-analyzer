import getpass
print("PASSWORD SECURITY ANALYZER")
print("----------------------")

password = getpass.getpass ("Enter a password to analyze: ")

print("password recieved securely!")
print("password length:", len(password))

#check password security requirements 
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)
has_length = len(password) >= 12

#calculate password strength score
score = 0 

if has_uppercase:
    score+= 1
if has_lowercase:
    score+= 1 
if has_number:
    score+= 1 
if has_special: 
    score+= 1
if has_length:
    score+= 1

    print("\nPASSWORD SECURITY RESULTS")
    print("----------------------")
    print("security score:", score, "/5")

    if score <=2:
        print("password strength: WEAK")
    elif score <=4: 
        print("password strength: MEDIUM")
    else:
        print("password strength: STRONG")    

#Give password improvement suggestions 

print("\nSECURITY RECOMMENDATIONS")
print("----------------------")

if not has_length:
    print("use at least 12 characters.")
if not has_uppercase:
    print("add an uppercase letter (A-Z).")
if not has_lowercase:
    print("add a lowercase letter (a-z).")
if not has_number:
    print("add a number (0-9).")
if not has_special:
    print("add a special character (e.g., !, @, #, $, %, ^, &, *).")
if score == 5:
    print("all basic requirements passed!")
    print("remember to use a uniqure, unpredictable password.")                