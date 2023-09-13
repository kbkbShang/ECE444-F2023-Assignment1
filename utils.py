class utils:
    def reversed(self, num):
        reverse = 0
        while num > 0:
            remainder = num % 10
            reverse = (reverse * 10) + remainder
            num = num // 10
        return reverse
    
    def formatter(self, num):
        result_base_2 = bin(num)
        result_base_8 = oct(num)
        return result_base_2, result_base_8