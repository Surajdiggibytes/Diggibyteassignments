import  util18
n = int(input())
emails = []
for i in range(n):
  email = input().strip()
  if util18.fun(email):
    emails.append(email)
print(sorted(emails))
#abc12@gmail.com abc10@gmail.com abc44@gmail.com