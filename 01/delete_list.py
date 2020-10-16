# 如何删除python list中的元素

# method 1
# h = [[1, 2], [3, 4], [5, 6]]
# h[0] = [8]
# print(h)


# method 2
# h = [[1, 2], [3, 4], [5, 6]]
# del h[0][1]
# print(h)

# method 3
h = [[1, 2], [3, 4], [5, 6]]
h[0].remove(1)
print(h)