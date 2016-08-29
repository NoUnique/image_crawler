confusion_table = [[2069, 63, 49, 130, 44, 48, 29, 29, 15],
                   [107, 2308, 21, 53, 35, 37, 17, 10, 24],
                   [138, 44, 1668, 238, 48, 83, 219, 66, 49],
                   [385, 107, 213, 2557, 50, 120, 143, 24, 43],
                   [152, 61, 39, 49, 1275, 64, 26, 12, 9],
                   [331, 131, 144, 277, 98, 2966, 94, 61, 40],
                   [137, 48, 177, 131, 48, 67, 1374, 31, 43],
                   [28, 6, 20, 6, 4, 15, 6, 1247, 11],
                   [157, 127, 200, 174, 44, 118, 137, 55, 2730]]


count_all = 0
count_correct = 0
for i in range(len(confusion_table)):
  for j in range(len(confusion_table[0])):
    count_all += confusion_table[i][j]
    if i==j:
      count_correct += confusion_table[i][j]

print float(count_correct) / float(count_all) * 100
    
