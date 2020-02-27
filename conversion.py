import random as r

#   This whole program is idea of 2d array . The 2d array(list) has 3 arrays(lists) with some random numbers inside.

#   Our goal is to sort even and non even numbers in special array for even and special array for odd numbers
#   There shouldnt be any duplicates .



#   Beginning of the first part of code.

#   Code is making 3 empty lists which will be made of some random numbers and added to the main list ..
#   So basicly we have 2d array.


twod_arr = []

for i in range(0,3):
    arr = []
    for j in range(0,5):
        var = r.randint(0,10)

        arr.append(var)

    twod_arr.append(arr)
print(twod_arr)



print("\n")
#End of the first "block" of code


#   Beginning of the second part of code.

#   We have our special arrays(lists) for even and odd numbers .. and we are looping through our main array , checking if its
#   divisible by 2 whitch is logicaly , even and appending in array for even numbers ,  else appending to odd numbers .

even_duplicates_numbers = []
odd_duplicates_numbers = []

for i in twod_arr:
    for j in i:
        if j % 2 == 0:
            even_duplicates_numbers.append(j)
        else:
            odd_duplicates_numbers.append(j)


print("\n")
#   End of the second "block" of code

#   Beginning of the third part of code.

#   Looping through both lists and removing possible zeros . We dont need them .

for i in even_duplicates_numbers:
    if i == 0:
        even_duplicates_numbers.remove(i)

for i in odd_duplicates_numbers:
    if i == 0:
        odd_duplicates_numbers.remove(i)


print(even_duplicates_numbers)
print(odd_duplicates_numbers)

print("\n")

#   End of the second "block" of code


#   Beginning of the fourth part of code.
#   This part of code , you figure it out !



even_numbers_without_duplicates = []
odd_numbers_without_duplicates = []

while len(even_duplicates_numbers) != 0:
    var1 = even_duplicates_numbers.pop()


    if var1 not in even_numbers_without_duplicates:
        even_numbers_without_duplicates.append(var1)

while len(odd_duplicates_numbers) != 0:
    var2 = odd_duplicates_numbers.pop()


    if var2 not in odd_numbers_without_duplicates:
        odd_numbers_without_duplicates.append(var2)


print(even_numbers_without_duplicates)
print(odd_numbers_without_duplicates)

# End of the fourth block of code

