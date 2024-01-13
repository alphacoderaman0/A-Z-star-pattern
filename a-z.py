#This is a Python code used to print the A-Z Star pattern.
n = (input("Enter any Alphabet: "))
if n == 'A' or n=='a':
    for row in range (7):
        for col in range(5):
            if (row==0) and (col in {1,2,3}):
                print("*" , end = " ")
            elif (row in {1,2,4,5,6}) and (col in {0,4}):
                print("*" , end = " ")
            elif (row==3):
                print("*" , end = " ")
            else:
                print(' ' , end=' ')
        print()
elif n == 'B' or n=='b':
    for row in range(7):
        for col in range(4):
            if row in {0,3,6} and col in {0,1,2} :
                print('*' , end=' ')
            elif row in {1,2,4,5} and col in {0,3} :
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()
elif n == "C"or n=="c":
    for row in range(6):
        for col in range(5):
            if row in {0,5} and col in {1,2,3,4} :
                print ('*' , end=' ')
            elif row in {1,2,3,4} and col==0 :
                print ('*' , end=' ')
            else:
                print (' ' , end=' ')
        print()

elif n == "D"or n=="d":
    for row in range(6):
        for col in range(5):
            if row in {0,5} and col in {0,1,2,3} :
                print('*' , end=' ')
            elif row in {1,2,3,4} and col in {0,4} :
                print('*' , end=' ')
            else :
                print(' ' , end=' ')
        print()

elif n == "E"or n=="e":
    for row in range(7):
        for col in range(5):
            if row in {0,3,6}:
                print('*' , end=' ')
            elif row in {1,2,4,5} and col==0:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "f"or n=="F":
    for row in range(7):
        for col in range(5):
            if row in {0,3}:
                print('*' , end=' ')
            elif row in {1,2,4,5,6} and col==0:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "g"or n=="G":
    for row in range(6):
        for col in range(6):
            if row==0 and col in {1,2,3,4}:
                print('*' , end=' ')
            elif row==1 and col in {0,5}:
                print('*' , end=' ')
            elif row==2 and col in {0}:
                print('*' , end=' ')
            elif row==3 and col in {0,3,4,5}:
                print('*' , end=' ')
            elif row==4 and col in {0,3,5}:
                print('*' , end=' ')
            elif row==5 and col in {1,2,5}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "H"or n=="h":
    for row in range(7):
        for col in range(6):
            if row==3:
                print('*' , end=' ')
            elif row in {0,1,2,4,5,6} and col in {0,5}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "I"or n=="i":
    for row in range(7):
        for col in range(7):
            if row in {0,6}:
                print('*' , end=' ')
            elif row in {1,2,3,4,5} and col in {3}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()
    
elif n == "J"or n=="j":
    for row in range(7):
        for col in range(7):
            if row==0:
                print('*' , end=' ')
            elif row in {1,2,3} and col==3:
                print('*' , end=' ')
            elif row in {4,5} and col in {1,3}:
                print('*' , end=' ')
            elif row==6 and col==2:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "K"or n=="k":
    for row in range(8):
        for col in range(6):
            if row in {0,6} and col in {0,5}:
                print('*' , end=' ')
            elif row in {1,5} and col in {0,4}:
                print('*' , end=' ')
            elif row==2 and col in {0,3}:
                print('*' , end=' ')
            elif row==3 and col in {0,2}:
                print('*' , end=' ')
            elif row==4 and col in {0,1,3}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n=='L' or n=='l':
    for row in range(7):
        for col in range(5):
            if col==0:
                print('*' , end=' ')
            elif row==6 and col in {1,2,3,4,5}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "m"or n=="M":
    for row in range(7):
        for col in range(7):
            if col in {0,6}:
                print('*' , end=' ')
            elif row==1 and col in {1,5}:
                print('*' , end=' ')
            elif row==2 and col in {2,4}:
                print('*' , end=' ')
            elif row==3 and col==3:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "N"or n=="n":
    for row in range(6):
        for col in range(6):
            if col in {0,5}:
                print('*' , end=' ')
            elif row==1 and col==1:
                print('*' , end=' ')
            elif row==2 and col==2:
                print('*' , end=' ')
            elif row==3 and col==3:
                print('*' , end=' ')
            elif row==4 and col==4:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "O"or n=="o":
    for row in range(6):
        for col in range(6):
            if row in{0,5} and col in {1,2,3,4}:
                print('*' , end=' ')
            elif row in {1,2,3,4} and col in {0,5}:
                print ('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "p"or n=="P":
    for row in range(7):
        for col in range(6):
            if col==0:
                print('*' , end=' ')
            elif row in {0,3} and col in {1,2,3,4}:
                print('*' , end=' ')
            elif row in {1,2} and col==5:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "Q"or n=="q":
    for row in range(7):
        for col in range(6):
            if row in {0,5} and col in{1,2,3,4}:
                print('*' , end=' ')
            elif row in {1,2} and col in{0,5}:
                print('*' , end=' ')
            elif row==3 and col in{0,2,5}:
                print('*' , end=' ')
            elif row==4 and col in{0,3,5}:
                print('*' , end=' ')
            elif row==6 and col==5:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "R"or n=="r":
    for row in range(7):
        for col in range(6):
            if col==0:
                print('*' , end=' ')
            elif row in {0,3} and col in {1,2,3,4}:
                print('*' , end=' ')
            elif row in {1,2} and col==5:
                print('*' , end=' ')
            elif row==4 and col==3:
                print('*' , end=' ')
            elif row==5 and col==4:
                print('*' , end=' ')
            elif row==6 and col==5:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "S"or n=="s":
    for row in range(7):
        for col in range(6):
            if row==0 and col in {1,2,3,4,5}:
                print('*' , end=' ')
            elif col==0 and row in {1,2}:
                print('*' , end=' ')
            elif row==3 and col in {1,2,3,4}:
                print('*' , end=' ')
            elif row in {4,5} and col==5:
                print('*' , end=' ')
            elif row==6 and col in {0,1,2,3,4}:
                print ('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "T"or n=="t":
    for row in range(7):
        for col in range(7):
            if row==1:
                print('*' , end=' ')
            elif col==3 and row in {1,2,3,4,5,6}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n == "U"or n=="u":
    for row in range(7):
        for col in range(6):
            if col in {0,5} and row in {0,1,2,3,4,5}:
                print('*' , end=' ')
            elif row==6 and col in {1,2,3,4}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n=='V' or n=='v' :
    for row in range(8):
        for col in range(13):
            if row==0 and col in {0,12}:
                print('*' , end=' ')
            elif row==1 and col in {1,11}:
                print('*' , end=' ')
            elif row==2 and col in {2,10}:
                print('*' , end=' ')
            elif row==3 and col in {3,9}:
                print('*' , end=' ')
            elif row==4 and col in {4,8}:
                print('*' , end=' ')
            elif row==5 and col in {5,7}:
                print('*' , end=' ')
            elif row==6 and col in {6,6}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n=='w' or n=='W' :
    for row in range(7):
        for col in range(7):
            if col in {0,6}:
                print('*' , end=' ')
            elif row==5 and col in {1,5}:
                print('*' , end=' ')
            elif row==4 and col in {2,4}:
                print('*' , end=' ')
            elif row==3 and col==3:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n=='X' or n=='x' :
    for row in range(6):
        for col in range(6):
            if row in {0,5} and col in {0,5}:
                print('*' , end=' ')
            elif row in {1,4} and col in {1,4}:
                print('*' , end=' ')
            elif row in {2,3} and col in {2,3}:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n=='Y' or n=='y':
    for row in range(7):
        for col in range(7):
            if row==0 and col in {0,6}:
                print('*' , end=' ')
            elif row==1 and col in {1,5}:
                print('*' , end=' ')
            elif row==2 and col in {2,4}:
                print('*' , end=' ')
            elif row==3 and col in {3,3}:
                print('*' , end=' ')
            elif row in {4,5,6} and col==3:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

elif n=='Z' or n=='z' :
    for row in range(7):
        for col in range(7):
            if row in {0,6}:
                print('*' , end=' ')
            elif row==1 and col==5:
                print('*' , end=' ')
            elif row==2 and col==4:
                print('*' , end=' ')
            elif row==3 and col==3:
                print('*' , end=' ')
            elif row==4 and col==2:
                print('*' , end=' ')
            elif row==5 and col==1:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        print()

else:
    print("Pattern Not Found")
