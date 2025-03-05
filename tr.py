# class Talaba:
#     def __init__(self, ism, yosh, baholar):
#         self.ism = ism
#         self.yosh = yosh
#         self.baholar = baholar  # Ro‘yxat shaklida

#     def ortacha_baho(self):
#         return sum(self.baholar) / len(self.baholar)

#     def yangi_baho_qosh(self, baho):
#         """Talabaga yangi baho qo‘shish metodi"""
#         self.baholar.append(baho)
#         print(f"{self.ism}ga {baho} bahosi qo‘shildi.")

#     def info(self):
#         """Talaba haqida umumiy ma'lumot chiqarish metodi"""
#         return f"Ism: {self.ism}, Yosh: {self.yosh}, O‘rtacha baho: {self.ortacha_baho():.2f}"

# # Obyekt yaratamiz
# talaba1 = Talaba("Ali", 20, [85, 90, 78])
# talaba2 = Talaba("Malika", 21, [92, 88, 95])

# # Obyektning ma'lumotlarini chiqaramiz
# print(talaba1.info())
# print(talaba2.info())

# # Talabaga yangi baho qo‘shamiz
# talaba1.yangi_baho_qosh(10)
# talaba2.yangi_baho_qosh(17)

# # Yangi o‘rtacha baholarni chiqaramiz
# print(talaba1.info())
# print(talaba2.info())


class Oquvchi:
    def __init__(self, ism,yosh,baho):
        self.ism= ism
        self.yosh=yosh
        self.baho=baho
    def get_ism(self):
        return self.ism
    def get_yosh(self):
        return self.yosh
    def get_baho(self):
        return self.baho
    def __repr__(self):
        return f"O‘quvchi: {self.ism}, Yosh: {self.yosh}, Baholar: {self.baho}"


oquvchi1 = Oquvchi('aziz',14,[5,5,5,4])
oquvchi2 = Oquvchi('nauriz',15,[5,4,5,4])
oquvchi3 = Oquvchi('dilshad',14,[5,5,5,5])
print(oquvchi1)
print(oquvchi2)
print(oquvchi3)
















