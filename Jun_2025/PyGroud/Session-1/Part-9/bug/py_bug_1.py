ids = ["XF345_89", "XER76849", "XA45A_55"]

x = 0
for id in ids:
    if "_" in id:
        x = x + 1

print(x)