class Calculator:

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

    def pov(self, a, b):
        return a ** b

    def avg(self, nums):
        if len(nums) == 0:
            return 0
        s = sum(nums)
        return self.div(s, len(nums))