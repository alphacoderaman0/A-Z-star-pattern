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