def plusOne(digits):
    digits=[str(i) for i in digits]
    digits=(''.join(digits))
    digits=int(digits)+1
    digits=[int(i) for i in str(digits)]
    print(digits)

plusOne([1,2,3])