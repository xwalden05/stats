def mean_stat(list):
    answer = 0 #Final value
    count = 0  #number of values

    ##Mean calculation
    for item in list:
        answer += item
        count +=1

    if(answer == 0):
        answer = "List is Empty"
        return answer
    else:
        answer = answer/count
        return answer


def main():
    li1 = {1,3,5}
    li2 = {2,4,6,8}
    li3 = {}

    print("Mean of list 1 = " +str(mean_stat(li1)))
    print("Mean of list 2 = " +str(mean_stat(li2)))
    #print("Mean of list 3 = " +str(mean_stat(li3)))

if __name__ == '__main__':
    main()
