import re

#Validate Email

'''with open("check_valid_emails.txt") as vaild_email:


    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+$")
    for emails in vaild_email:
        email = emails.strip()
        #print(email)
        if pattern.fullmatch(string=email):

            print(f"{email} is a Valid Email")
        else:
            print(f"{email} is not a Valid Email")

'''
#[\w\.-]+

#[...]: A character class (match any one of the characters inside)

#\w: Matches any word character — same as [a-zA-Z0-9_]

#.: A literal dot (escaped as \. to avoid meaning "any character")

#-: A literal dash

#+: Means one or more of the preceding group


#Match Date in YYYY-MM-DD Format

date = "26-06-1998"

pattern = re.compile(r"^\d{2}-\d{2}-\d{4}$")

if pattern.match(string=date):
    print(f"Pattern Matched")

else:
    print(f"Pattern is not Matched")

