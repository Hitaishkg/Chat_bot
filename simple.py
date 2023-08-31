x = 11
for i in range(x):
    for j in range(11):
        for k in range(x):
            print(f"{i+k}x{j}={(i+k)*j}\t",end=" ")
        print("")
    break 