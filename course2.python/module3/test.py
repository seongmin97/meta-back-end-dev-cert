a = [[96], [69]]

print(''.join(list(map(str, a))))

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)