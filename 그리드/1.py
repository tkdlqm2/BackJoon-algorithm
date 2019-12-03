def compareWord(input1,input2):
    list = []
    result = 0
    j = 0
    if len(input1) == len(input2): # 문자열의 길이가 같은 경우
        for i in range(0,len(input1)):
            if input1[i] == input2[i]:
                result += 1
        return len(input2) - result

    else:
        while True:
            result = 0
            for i in range(0,len(input2)):
                try:
                    if input1[i] == input2[i+j]:
                        result += 1 # 문자가 겹치는 수
                except:
                    continue
            list.append(result)
            if len(input1) + j == len(input2):
                return len(input1) - max(list)
            j += 1


answer = 0
inputText1, inputText2 = input().split()
inputText1 = list(inputText1)
inputText2 = list(inputText2)

print(compareWord(inputText1,inputText2))
