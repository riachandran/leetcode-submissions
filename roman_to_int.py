class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sub_mapper = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        inp_list = [i for i in s]
        sum = 0
        for idx,val in enumerate(inp_list):
            if(idx != len(s) - 1):
                dual_roman = inp_list[idx]+inp_list[idx+1]
                print(dual_roman)
                if dual_roman in sub_mapper:
                    sum += sub_mapper[dual_roman] - mapper[inp_list[idx+1]]
                elif dual_roman not in sub_mapper:
                    sum += mapper[val]
            else:
                sum += mapper[val]
        return sum
        
