para = input("Enter paragraph: ")

words = para.lower().split()
print(words)
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

most_occurred = max(count, key=count.get)

print("Most occurred word:", most_occurred)
print("Occurrence:", count[most_occurred])