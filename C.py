for row in range(6):
    for col in range(5):
        if row in {0,5} and col in {1,2,3,4} :
            print ('*' , end=' ')
        elif row in {1,2,3,4} and col==0 :
            print ('*' , end=' ')
        else:
            print (' ' , end=' ')
    print()

