def count_letters(word):
    count = {}
    for letter in word:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

# Test the function
result = count_letters("hello")
print(result)