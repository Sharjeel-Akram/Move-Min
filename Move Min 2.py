# Write a python program which takes two lists list1 (sorted) and list2 (unsorted) as input 
# and returns a sorted list which contains elements of list1 and list2.
# Sample Input: list1 = [5,10,15,20,25] and list2 = [6,7,13,9,1,4]
# Expected Output: [1,4,5,6,7,9,10,13,15,20,25]

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
    List1 = [15,35,45,48,55,68,75,98]
    print("Here Is Given Below the First Sortted List:  ")
    print(List1)
    List2 = []
    Total_Numbers2 = input("How many numbers you want to add in List2: ")
    print("Enter your numbers for List2: ")
    for i in range(int(Total_Numbers2)):
        N = int(input(" "))
        List2.append(N)
    print("Here Is Given Below the Second Unsorted List:  ")
    print(List2)
    Final_List(List1,List2)   
Take_Input()