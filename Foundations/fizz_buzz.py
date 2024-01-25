"""
Question:
- Fizz Buzz is a game for two or more players.
- Take it in turns to count aloud from 1 to 100, but each time you are going to say a multiple of 3, 
  replace it wutg the word 'fizz'. 
- For multiples of 5, say 'buzz', and for numbers that are multiples of both 3 ans 5, say 'fizz, buzz'

"""
count_until = 16

numbers = [0]*(count_until+1)
for num in range(1,count_until+1):
    if num % 3 == 0:
        numbers[num] = "fizz"
        if num % 5 == 0: 
            numbers[num] = "fizz, buzz"
    elif num % 5 == 0: 
        numbers[num] = "buzz"
    else: 
        numbers[num] = num

print(numbers)
    

# if we want to print the output instead of making it a list, the order or the if conditions matters. 
