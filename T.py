for row in range(7):
    for col in range(7):
        if row==1:
            print('*' , end=' ')
        elif col==3 and row in {1,2,3,4,5,6}:
            print('*' , end=' ')
        else:
            print(' ' , end=' ')
    print()
