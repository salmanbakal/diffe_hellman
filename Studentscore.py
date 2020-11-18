File = open('scores.csv','r')
data = File.readlines()

data = [line.strip() for line in data]

heading = data[0].split(",")
data = data[1:]
total_subjects = len(heading)

marks = {}
marksmax=0

for i in range(len(data)):
    score = data[i].split(',')
    marks[score[0]] = sum([int(j) for j in score[1:]])

for name in marks.keys():
    print(f'{name}: {marks[name]}')
    if marks[name] > marks[score[0]]:
        print(f'highest marks is {marks[name]} scored by {name}')
        



