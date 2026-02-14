while True:
 
 email = input("Enter your email: ")
 print("===============================")
 a,b,c = 0,0,0
 if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and email.count("@") == 1:
            if email[-3] == "." or email[-4] == ".":
                for i in email:
                    if i.isspace():
                        a=1
                    
                    elif not (i.isalpha() or i.isdigit() or i in "@._"):
                        c=1
                if a==1  or c==1:
                    print("Contains invalid characters and spaces")
                    print("===============================")
                else:
                    print("Right email") 
                    print("===============================")
                    break
            else:
                print("Wrong email (.) at wrong position")
                print("===============================")
        else:
            print("Wrong email: (@) should be used 1 time") 
            print("===============================")
    else:
        print("Wrong email:Email sould start from an alphabet")
        print("===============================")
 else:
    print("Wrong email: Too short at least 6 digit")
    print("===============================")


   
















