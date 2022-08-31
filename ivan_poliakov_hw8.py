import datetime

"""task 1"""
num1 = input("print number 1 \n")
num2 = input("print number 2 \n")
num3 = input("print number 3 \n")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
def int_args(n1, n2, n3):
    max_args = max(n1, n2, n3)
    return max_args
print("Найбольшее число: ", int_args(num1, num2, num3))

"""task 2"""
one = 7
two = 2
three = 22
def finding_max_tw(one, two):
    max_args1 = max(one, two)
    return max_args1
print("Найбольшее число из двух: ", finding_max_tw(one, two))

def finding_max_three(one, two, three):
    middle = finding_max_tw(one, two)
    return finding_max_tw(middle, three)
print("Найбольшее число из трех: ", finding_max_three(one, two,three))


"""task 3"""
tuple_1 = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]

tuple_1.sort(key=lambda x: x[1])
print(tuple_1)

"""task 4"""
now = datetime.datetime.now()
year = lambda now: now.strftime("%Y")
print(year(now))
month = lambda now: now.strftime("%B")
print(month(now))
day = lambda now: now.strftime("%d")
print(day(now))
#documentation datatime:
# https://docs.python.org/3/library/datetime.html