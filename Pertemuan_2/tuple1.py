tuple1 = (4,5,3,"abc")
print(tuple1)

list1 = [3,4,5,"abc"]
print(list1)
a,*b,c = tuple1
print(b)

for x in reversed(list1):
    print(x)

test_list = [(2, 4), (5, 9), (13, 17), (24, 27)]
for x,y in reversed(test_list):
    print("x: {}, y: {}".format(x,y))

test_str = "geeksforgeeks is best for geeks and programming"
print(test_str[:24])
print(test_str[27 + 1:])
print(test_str[28:])

for front, rear in reversed(test_list):
    test_str = test_str[: front] + test_str[rear + 1:]
    print("test_str: {}".format(test_str))


