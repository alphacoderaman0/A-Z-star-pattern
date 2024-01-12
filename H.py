for row in range(7):
    for col in range(6):
        if row==3:
            print('*' , end=' ')
        elif row in {0,1,2,4,5,6} and col in {0,5}:
            print('*' , end=' ')
        else:
            print(' ' , end=' ')
    print()