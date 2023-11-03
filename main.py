cals = open("input.txt")

elves = cals.read().split("\n\n")
elves = [i.split('\n') for i in elves]
mostCals = 0
totalCals = []
topThreeSum = 0

for i in range(len(elves)):
    for j in range(len(elves[i])):
        elves[i][j] = int(elves[i][j])
    if sum(elves[i]) > mostCals:
        mostCals = sum(elves[i])
    totalCals.append(sum(elves[i]))

totalCals.sort(reverse=True)
for i in range(3):
    topThreeSum += totalCals[i]

print(f'Most calories carried: {mostCals}')
print(f'Top three elves calories: {topThreeSum}')
