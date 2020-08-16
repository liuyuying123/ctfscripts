import re
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
first_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","babaa","babab","babba","babbb","bbaaa","bbaab"]
second_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","baabb","babaa","babab","babba","babbb"]
print(len(first_cipher))

def encode():
    string=input("Please input string to encode:\n")
    e_string1=""
    e_string2=""
    for alpha in string:
        index=alphabet.index(alphabet)
        e_string1+=first_cipher[index]
        e_string2=second_cipher[index]
    print("first encode method result is:\n"+e_string1)
    print("second encode method result is:\n"+e_string2)
    return 

def decode():
    e_string=input("Please input string to decode:\n")
    e_array=re.findall(".{5}",e_string)#e_string作为一个列表
    d_string1=""
    d_string2=""
    for k in e_array:
        index1=first_cipher.index(k)
        d_string1+=alphabet[index1]
        index2=second_cipher.index(k)
        d_string2+=alphabet[index2]
    print("first decode method result is: "+d_string1)
    print("second decode method result is: "+d_string2)
    return 

if __name__=='__main__':
    while True:
        number=input("encode 1,decode 2:\n")
        number=int(number)
        if number==1:
            encode()
        elif number==2:
            decode()
        else:
            break
