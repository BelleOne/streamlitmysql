
def checkberdees(phone_number):
    total = 0

    predict = ""

    for phone in phone_number:
        total += int(phone)

        print(total)

        if total in (9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65):
            predict = "ระดับดีมาก"
        elif total in (69, 79):
            predict = "โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย"
        elif total in (10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61):
            predict = "ระดับดีปานกลาง"
        elif total in (62, 66, 68, 74, 75):
            predict = "เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ"
        elif total in (11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80):
            predict = "ระดับไม่ดี"
        else:
            predict = "ไม่สามารถวิเคราะห์ได้"
            return predict


phone_number = input('enter phone number ')
print(checkberdees(phone_number))
