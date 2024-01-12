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