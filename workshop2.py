name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height in centimeters: ")
power = input("Enter your power (1-10): ")
balance = input("Enter your balance (Starter Pack Dollar): ")

if int(age) > 27 and int(height) > 165 and int(power) < 7 and int(balance) > 1000:
    print("ตำแหน่งของคุณคือ ผู้รักษาความปลอดภัยของข้อมูล")
elif int(age) > 25 and int(height) >= 170 and int(power) >= 9 and int(balance) >= 1000:
    print("ตำแหน่งของคุณคือ กำลังเสริมฝ่ายต่อสู้")
elif int(age) > 22 and int(height) > 150 and int(power) > 4 and int(balance) > 3000:
    print("ตำแหน่งของคุณคือ แฮ็กเกอร์")
else:
    print("ไม่ผ่านการคัดเลือก")
