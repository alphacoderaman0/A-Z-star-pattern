for row in range(6):
    for col in range(6):
        if row in {0,5} and col in {0,5}:
            print('*' , end=' ')
        elif row in {1,4} and col in {1,4}:
            print('*' , end=' ')
        elif row in {2,3} and col in {2,3}:
            print('*' , end=' ')
        else:
            print(' ' , end=' ')
    print()