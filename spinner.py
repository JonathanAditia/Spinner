oriList = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

def counterClockwise(data): #function
    
    emptyList1 = [] #list kosong utk menampung masing2 data yg akan di tukarkan
    emptyList2 = []
    emptyList3 = []
    for i in range(0,3): #loop 3x (sebanyak data)
        emptyList1.append(data[i][0]) #append data [0-2][0] ke list 1
        emptyList2.append(data[i][1]) #... [0-2][1]...2
        emptyList3.append(data[i][2]) #... [0-2][2]...3
        
        mainList = [emptyList3, emptyList2, emptyList1] #kumpulkan dan urutkan smua emptyList
        
    return mainList #hasil

    
counterClockwise(oriList)
