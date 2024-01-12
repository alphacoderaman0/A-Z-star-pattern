for row in range(7):
    for col in range(6):
        if col in {0,5} and row in {0,1,2,3,4,5}:
            print('*' , end=' ')
        elif row==6 and col in {1,2,3,4}:
            print('*' , end=' ')
        else:
            print(' ' , end=' ')
    print()