class Solution:
    def decode(s):
        s = s[::-1]
        current = ''
        res = ''
        for i in range(len(s)):
            #add number to current
            current += s[i]
            print(current)
            #if we can convert, do so and reset current
            ascii = int(current)
            print("ascii: ", ascii)
            if (ascii >= 65 and ascii <= 90) or (ascii >=97 and ascii <= 122) or ascii == 32:
                res += chr(ascii)
                current = ''
        return res


    

    print(decode("23511011501782351112179911801562340161171141148"))
