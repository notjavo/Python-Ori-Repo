def sum_of_multiples(limit):
    #initalize the sum
    total_sum=0

    #loop through each number from 1 to limit -1
    for number in range(limit):
        #belowing checking if the number is a multiple of three and five
        if number % 3 == 0 or number % 5 == 0:
            #next, adding the number to total sum
            total_sum += number

        return total_sum
    
    #next I will define the limit
    limit=1000

    #calling the funtion and printing the result
    result = sum_of_multiples
    print(f"The sum of all multiples of 3 and 5 below {limit} is {result}")