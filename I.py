for row in range(7):
    for col in range(7):
        if row in {0,6}:
            print('*' , end=' ')
        elif row in {1,2,3,4,5} and col in {3}:
            print('*' , end=' ')
        else:
            print(' ' , end=' ')
    print()