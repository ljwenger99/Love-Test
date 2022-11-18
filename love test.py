def matchmaker():
    #get the names
    n1 = input('Who is the first potential lovebird? ')
    n2 = input('And the second? ')

    #score the names
    n1s = 0
    n2s = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in n1:
        if i in vowels:
            n1s += 5
        else:
            if i.isalpha() == True:
                n1s -= 1
            elif i.isalpha() == False:
                continue
    for i in n2:
        if i in vowels:
            n2s += 5
        else:
            if i.isalpha() == True:
                n2s -= 1
            elif i.isalpha() == False:
                continue
            
    #print the names
    print(n1,n1s)
    print(n2,n2s)

    #compare  the scores/print statement
    if abs(n1s - n2s) <= 5:
        print("You're soulmates!!!")
    elif 6 <= abs(n1s - n2s) <= 10:
        print("Eh, you're a decent match.")
    else:
        print("It's not meant to be. Find someone else.")
