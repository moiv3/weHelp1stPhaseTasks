def reverseString(s):
    # 你的程式碼
    thing = ""
    for i in range(len(s)):
        thing += s[len(s)-i-1]
    return thing
print(reverseString("TASER"))

def formatFloat(n):
    # 你的程式碼
    return "{:.2f}".format(n)

print(formatFloat(3.465))
print(formatFloat(4.5))
print(formatFloat(3))

def getChineseZodiac(year):
    result = (year - 1912) % 12
    if result == 0:
        return "鼠"
    elif result == 1:
        return "牛"
    elif result == 2:
        return "虎"
    elif result == 3:
        return "兔"
    elif result == 4:
        return "龍"
    elif result == 5:
        return "蛇"
    elif result == 6:
        return "馬"
    elif result == 7:
        return "羊"
    elif result == 8:
        return "猴"
    elif result == 9:
        return "雞"
    elif result == 10:
        return "狗"
    else:
        return "豬"
    
    
    # 你的程式碼

def checkPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            return False
    return True
print(checkPalindrome("AAABA"))

def calculate(n1, n2, op):
    import math
    # 你的程式碼
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return math.floor(n1/n2)


def snakeToUpperCamel(name):
    output_string = ""
    flag = 0
    for i in range(len(name)):
        if i == 0:
            output_string += name[i].upper()
            print(output_string)
        elif flag == 1:
            output_string += name[i].upper()
            flag = 0
        elif name[i] == "_":
            flag = 1
        else:
            output_string += name[i]

    return output_string

print(snakeToUpperCamel("agh_jhj_ksk"))