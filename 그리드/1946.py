# 컨셉 1: 1등 서류 성적의 면접 성적을 기준을 잡고 그것 보다 낮은 순위의 지원자를 지운다.
# 컨셉 2 :1번 과정에 해당되는 지원자들을 토대로 면접 성적 1등을 기준을 잡고 그것 보다 낮은 순위의 지원자를 지운다.

num1 = int(input())
answer = []

for i in range(0,num1):
    num2 = int(input())
    specialNumber = 0
    list = []
    first = '1'
    firstPartner = ''
    secondPartner = ''
    seconde = 1

    for j in range(0,num2):
        inputData = input().split()
        list.append(inputData)

        if inputData[0] == '1':
            firstPartner = inputData[1] # 1등 서류 성적의 면접 성적.
        if inputData[1] == '1':
            secondPartner = inputData[0] # 1등 면접 성적의 서류 성적

    count = 2 # 서류 1등 점수와 면접 1등은 무조건 합격이기에 초기화는 2

    for k in range(0,len(list)):
        if firstPartner > list[k][1]: # 1등 서류 성적의 면접 성적을 기준으로 거른다. (컨셉1)
            if secondPartner > list[k][0]: # 1등 면접 성적의 서류 성적을 기준으로 거른다 (컨셉2)
                count += 1

    print(count)