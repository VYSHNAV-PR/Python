
# def compress(s):
#     result = ""
#     count = 1

#     for i in range(1, len(s)):
#         if s[i] == s[i-1]:
#             count += 1
#         else:
#             if count > 2:
#                 result += s[i-1] + str(count)
#             else:
#                 result += s[i-1] * count
#             count = 1

#     # for last character group
#     if count > 2:
#         result += s[-1] + str(count)
#     else:
#         result += s[-1] * count

#     return result


# Example
# letter=input("Enter the string:")
# print(compress(letter))


s = input("Enter string:")
s = list(s)

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        for j in range(i+2, len(s)):
            if s[j] != s[i]:
                s[i+1], s[j] = s[j], s[i+1]
                break

result = "".join(s)
print(result)           