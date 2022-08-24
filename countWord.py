# text = 'The quick brown fox jumps over the lazy dog'

# print(len(text.split()))


# bucket_list = 'Japan, Singapore, Maldives, Europe, Italy, Korea'

# result = bucket_list.split(',')
# print(len(result))

bucket_list = 'Japan, Singapore, Maldives, Europe, Italy, Korea'

# comma delimiter
result = len(bucket_list.split(',', 3))

# Prints an array of strings
print(bucket_list.split(',', 3))

print("There are " + str(result) + " words.")