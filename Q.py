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