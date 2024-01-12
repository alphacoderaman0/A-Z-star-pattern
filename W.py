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