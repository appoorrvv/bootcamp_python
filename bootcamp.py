# Read a list of integers from user input.
# Find all pairs of numbers in the list whose product is even and whose sum is odd.
# Print out a formatted list of the pairs.

int_list=[]

input_value=input("Enter integers seperated by space:  ")
new_list=input_value.split()
product_list=[]
product=0
for i in range(len(new_list)):
  for j in range(i+1,len(new_list)):
      product=int(new_list[i])*int(new_list[j])
      if product%2==0:
        product_list.append([new_list[i],new_list[j]])
new_list=[]
for i in product_list:
  if (int(i[0])+int(i[1]))%2!=0:
    new_list.append([i[0],i[1]])
print(new_list)