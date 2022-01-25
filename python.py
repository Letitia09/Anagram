def check_anagram(data1,data2):
    #start writing your code here
    a1=data1.lower()
    a2=data2.lower()
    flag=True
    if len(a1)==len(a2):
        for i in range(len(a1)):
            if a1[i]==a2[i] or a1[i] not in a2 or a2[i] not in a1:
                flag=False
                break
            else:
                flag=True
    else:
        flag=False
    return flag              
print(check_anagram("scller","resell"))
