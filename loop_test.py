x1 = [1, 3,5]
y1 = [9, 12, 13]
L = [x **2 for (x,y) in zip(x1, y1) if y > 10]
print L

G = (x for x in range(4))
print type(G)