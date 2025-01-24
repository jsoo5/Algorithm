characters = []
cnt = 0
result = ''

for i in range(5):
    inputs = list(input())
    characters.append(inputs)
    cnt += len(inputs)

rows = len(characters)

while len(result) != cnt:
    for row in range(rows):
        try:
            result += characters[row][0]
            del characters[row][0]
        except:
            continue
print(result)