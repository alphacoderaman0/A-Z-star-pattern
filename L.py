for row in range(7):
    for col in range(5):
        if col==0:
            print('*' , end=' ')
        elif row==6 and col in {1,2,3,4,5}:
            print('*' , end=' ')
        else:
            print(' ' , end=' ')
    print()