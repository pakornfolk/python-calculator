class Calculator:
    def add(self, a, b):
        return a + b 

    def subtract(self, a, b):
        return a - b # แก้จาก b - a ให้เป็น a - b

    def multiply(self, a, b):
        result = 0
        for _ in range(b): # ใช้ range(b) เพื่อให้ไม่เกินรอบ
                result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        while a >= b: # แก้จาก while a > b ให้เป็น a >= b
            a = self.subtract(a, b)
            result += 1
        return result

    def modulo(self, a, b):
        while a >= b: # แก้จาก while a <= b ให้เป็น a >= b
            a = a - b
        return a