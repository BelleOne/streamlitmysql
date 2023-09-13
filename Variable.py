# สร้างตัวแปรเก็บข้อมูล

a = 10
b = 3.14
c = "Hello"

print(type(a))
print(type(b))
print(type(c))


print(a + b)
# print(a + c)

print(int(b))
print(float(a))


status = True

msg = False

print(status)
print(msg)

print(type(msg))

# 1=True 0=False
print(status == 1)
print(msg == 0)

# แสดงผลตัวแปรรวมกับข้อความ

price = 100.60
qty = 7

print("ราคาสินค้า", price, "บาท", "จำนวน", qty, "ชิ้น")

print("ราคาสินค้า %.2f บาท จำนวน %d ชิ้น" % (price, qty))

print(f"ราคาสินค้า {price:.2f} จำนวน  {qty} ชิ้น")
