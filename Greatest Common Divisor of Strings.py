def gcd(a,b):  
    return abs(a) if b == 0 else gcd(b, a%b)
def gcdOfStrings(str1, str2):
    if str1+str2 != str2+str1:
        return ""
    m=gcd(len(str1),len(str2))
    return str1[:m]

print(gcdOfStrings("ABCABC","ABC"))
        