for i in range(1, 10):
    if i == 5:
        break
    print("Stopped at", i)
for i in range(1, 10):
    if i == 5:
        continue
    print("Skipped 5 ->", i)
