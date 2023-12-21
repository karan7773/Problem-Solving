def multiply(num1, num2):
    num1=eval(num1)
    num2=eval(num2)
    res=num1*num2
    print(type(res),res)
    res="% s" % res
    print(type(res),res)

print(multiply("123","456"))