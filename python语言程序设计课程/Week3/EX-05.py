'''凯撒密码是古罗马凯撒大帝用来对军事情报进行加解密的算法，它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，即，字母表的对应关系如下：
原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
对于原文字符P，其密文字符C满足如下条件：C=(P+3) mod 26
上述是凯撒密码的加密方法，解密方法反之，即：P=(C-3) mod 26
假设用户可能使用的输入仅包含小写字母a~z和空格，请编写一个程序，对输入字符串进行凯撒密码加密，直接输出结果，其中空格不用进行加密处理。使用input()获得输入。
 '''
def Kaisa(source):
    kaisa=''
    for i in source:
        if i==' ':
             kaisa=kaisa +' '
        else:
            kaisa=kaisa + chr( ( ord(i)-ord('a') + 3) % 26+ord('a'))
    return kaisa

def getKaisa(kaisa):
    getkaisa=''
    for i in kaisa:
        if i==' ':
            getkaisa=getkaisa+' '
        else:
            getkaisa=getkaisa+ chr( (ord(i)-ord('a')-3) %26 +ord('a'))
    return getkaisa

code=input()
print(Kaisa(code))
print(getKaisa(Kaisa(code)))
#print(ord('a'))



