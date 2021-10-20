passwords = input().split()
passwords.sort(key=len)
for password in passwords:
    print(password, len(password))
