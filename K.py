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