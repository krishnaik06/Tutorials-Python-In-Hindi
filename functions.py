## why functions?(Interview Question)
# 1. to make code more readable
# 2. to make code more efficient
# 3. to make code more maintainable
# 4. to make code more reusable
# 5. to make code more extensible


# function

def welcome(msg)->str:
    """
    Description: This function will show a welcome message
    

    Return : This function will return the welcome message 
    """



    return msg



msg=welcome("Welcome all")
print(msg + "Please subscribe")



## function to add even and odd number

def even_odd_sum(lst):
    """
    Description: This function will add even and odd number in a list
    Return : This function will return the sum of even and odd number in a list
    """

    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return even_sum,odd_sum


sum1,sum2=even_odd_sum([1,2,3,45,6,677,7,8,8,54,4,3,5,6])
print(sum1,sum2)
