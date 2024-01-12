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