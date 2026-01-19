# #You are given a sentence. Reverse each word individually while keeping the word order the same.

# def word_revserse(sentence):
#     words=sentence.split()
#     reverse_words=[word[::-1] for word in words]
#     return ' '.join(reverse_words)
# string=input("Enter the string:")
# print(f"Reverse:{word_revserse(string)}")

# strs =  ["dog","racecar","car"]
# if not strs:
#     print("")
# else:
#     prefix = strs[0]
#     for s in strs[1:]:
#         i = 0
#         while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
#             i += 1
#         prefix = prefix[:i]
#         if not prefix:
#             print("")
#             break
#     else:
#         print(prefix)