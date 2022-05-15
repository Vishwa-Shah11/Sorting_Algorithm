def combinationSort(strList):
    L1 = []
    L2 = []
    tempLst = []
    lstDict = {}

    '''
    for i in range(len(strList)):
        first = strList[i][0]
        print(first)
        tempLst.append(first)
        tempLst.sort()
        print(tempLst)
        rest = strList[i][1:]
        print(rest)
    ''' 
    #strList.sort(key = str)
    #L1 = strList
    #print(strList)
    for i in strList:
        sum = 0
        for j in i:
            print(j) 
            print(ord(j))
            sum += ord(j)
        #print(sum)
        tempLst.append(sum)
        #print(tempLst)
        tempLst.sort()
        print(tempLst)
        if i in lstDict.keys():
            lstDict.update({i:sum})
        else:
            lstDict[i] = sum

        print(lstDict)

        print(sorted(lstDict.items(), key = lambda a : (a[1], a[0])))
        



print(combinationSort(['d34', 'g54', 'd12', 'b87', 'g1', 'c65', 'g40', 'g5', 'd77']))
    