
        # outer loop
for outer_number in range(2,101):

    # inner loop - see if any of these numbers divides outer number
    if_prime = True
    
    for inner_number in range(2, outer_number):

        # if it does, go on to next number
        if outer_number % inner_number == 0:
            if_prime = False
            break

    # if reach her, the outer number doesn't divide by any of the 
    # inner numbers, so it was prime
    if if_prime:
        print(outer_number)





#integer % inner_loop == 0:
    #print(integer)
#if integer == 200:
    #print("Only up to 100")