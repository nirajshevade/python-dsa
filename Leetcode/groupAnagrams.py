def groupAnagrams(strs):
    groups = {}
    for word in strs:
        count = [0] * 26
        for char in word:
           index = ord(char) - ord('a')
           count[index] += 1
        key = tuple(count)
        
        if key not in groups:
            groups[key] = []
        
        groups[key].append(word)
    return list(groups.values())

str = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(str))