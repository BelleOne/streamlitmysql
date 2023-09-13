print("Login System")

# การรับค่าจากผู้ใช้งาน
username = input('Username:')
password = input('Password:')
print(username)
print(password)

# ตรวจเงื่อนไขการ login
if username.strip().lower() == "admin" and password == "1234":
    print("Login Success")
else:
    print("Login Failure")
