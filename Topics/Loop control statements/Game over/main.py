scores = input().split()
# put your python code here
count = 0
lose = 0
for score in scores:
    if lose > 2:
        break
    if score == 'C':
        count += 1
    else:
        lose += 1
print("You won" if lose < 3 else "Game over")
print(count)