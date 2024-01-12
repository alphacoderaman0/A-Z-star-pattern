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