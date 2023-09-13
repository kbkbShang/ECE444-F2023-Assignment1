class utils:
    def reversed(self, num):
        reverse = int(str(num)[::-1])
        return reverse
    
    def formatter(self, num):
        result_base_2 = bin(num)
        result_base_8 = oct(num)
        return result_base_2, result_base_8