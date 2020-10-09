def mean_stat(list):
    """
    Calulates the mean of the list provided.
    doctest verifies functions are getting correct values

    >>> mean_stat([5,3,17])
    8.333333333333334
    >>> mean_stat([5])
    5.0
    >>> mean_stat([-1,4,.5,2.5])
    1.5
    """
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


def median_stat(list):
    """
    Calculates the median of a given List
    doctest verifies median is calculated correctly

    >>> median_stat([5,3,17])
    5
    >>> median_stat([-7])
    -7
    >>> median_stat([11,8,5,2])
    6.5
    >>> median_stat([-1,4,.5,2.5])
    1.5
    """

    list.sort()
    length = len(list)
    answer = 0
    if(length % 2 == 0):
        mid1 = list[length//2]
        mid2 = list[length//2-1]
        return (mid1 +mid2)/2
    else:
        return list[length//2]

    ##return answer


def main():
    import statistics
    li1 = [1,3,5]
    li2 = [2,4,6,8]
    li3 = []

    print("Mean of list 1 = " +str(mean_stat(li1)))
    print("Mean of list 2 = " +str(mean_stat(li2)))
    #print("Mean of list 3 = " +str(mean_stat(li3)))
    print("Median of list 1 = "+str(median_stat(li1)))
    print("Median of list 2 = "+str(median_stat(li2)))

if __name__ == '__main__':
    main()
