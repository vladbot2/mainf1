# def elements(list):
#     product = 1
#     for num in list:
#         product *= num
#     return product

#2
# def min(list):
#     if not list:
#         return None
#     minimum = list[0]
#     for num in list:
#         if num < minimum:
#             minimum = num
#     return minimum

#3
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def primes(lst):
#     return sum(1 for num in lst if prime(num))


#4
# def remove(list, number):
#     initiali = len(list)
#     list[:] = [num for num in list if num != number]
#     return initiali - len(list)

#5
# def merge(list1, list2):
#     return list1 + list2

#6
# def elements(list, power):
#     return [num ** power for num in list]




