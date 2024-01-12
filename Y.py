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