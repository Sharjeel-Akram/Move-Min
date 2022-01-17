# Write a python program which takes two unsorted listslist1 and list2 as input and returns 
# a sorted list which contains elements of list1 and list2.
# Sample Input: list1 = [12,33,42,1,23,3] and list2 = [11,5,67,87,2,13,15]
# Expected Output: [1,2,3,5,11,12,13,15,23,33,42,67,87]

def Move_Min(Values,Index):
    Min_Index = Index
    Start_Value = Values[Index]
    for i in range(Index,len(Values)):
        if Values[i] < Values[Min_Index]:
            Min_Index = i       
    Values[Index] = Values[Min_Index]
    Values[Min_Index] = Start_Value
    return(Values)
def Selection_Sort(Final_List):
    for i in range(len(Final_List)-1):
        Move_Min(Final_List,i)
    print("The Sorted List is Given Below: ")
    print(Final_List)
def Final_List(L1,L2):
    Final_List = L1 + L2
    print("Here Is Given Below the Combined Unsorted List:  ")
    print(Final_List)
    (Selection_Sort(Final_List))
def Take_Input():
    List1 = []
    List2 = []
    Total_Numbers1 = input("How many numbers you want to add in List1: ")
    print("Enter your numbers for List1: ")
    for i in range(int(Total_Numbers1)):
        N = int(input(" "))
        List1.append(N)
    Total_Numbers2 = input("How many numbers you want to add in List2: ")
    print("Enter your numbers for List2: ")
    for i in range(int(Total_Numbers2)):
        N = int(input(" "))
        List2.append(N)   
    print("Here Is Given Below the First Unsorted List:  ")
    print(List1)
    print("Here Is Given Below the Second Unsorted List:  ")
    print(List2)
    Final_List(List1,List2)
Take_Input()
