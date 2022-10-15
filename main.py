numbers = [     [10, 11, 12, 13, 14],
               [20, 21, 22, 23, 24],
               [30, 31, 32, 33, 34]]

#numbers =[] 
#rnum = int(input('Enter the number of rows'))
#for i in range(rnum):
 #row = list(map(int, input('Enter 5 values for a row: ').split()))
 #numbers.append(row)

rnum = len(numbers)
cnum = len(numbers[0])

# ******************************
# Make your Code
# ******************************
for i in range (rnum):
    rsum = 0
    for j in range(cnum):
        rsum += numbers[i][j]
    print(f'The summation of row{i}: {rsum}')
