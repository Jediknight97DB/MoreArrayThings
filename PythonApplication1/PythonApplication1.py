mylist1 = [1,7,4,5,6]
mylist2 = [2,3,4,4,7]
mylist3 = [4,7,2,9,5]

sum1 = 8
def hashtable_sum_solution(*mlst):
    mydict = {}
    qt = "i"
    while True:
        qt = "run the no pairs"
        try:
            index = int(input("Which list do you wish to access: ")) - 1
            if int(index + 1) > len(mlst):
                raise ValueError("Numbers larger than " + str(len(mlst)) + " are not accepted!")
        except ValueError as er:
            print(er + "/n Restart the Program!")
        else:
            print("List number " + str(index + 1) + " is being assessed:")
        for i in mlst[index]:
              if i in mydict:
                 print("Sum of " + str(sum1 - i) + " & " + str(i) + " is equal too: " + str(sum1))
                 qt = str(input("Type q to quit: "))
                 if qt == "q":
                    return True        
              else:
                 mydict[sum1 - i] = True
        if qt == "run the no pairs":
            print("No pair of numbers equal to the sum was found.")
            qt = str(input("Type q to quit: "))
            if qt == "q":
                return False

print(str(hashtable_sum_solution(mylist1, mylist2, mylist3)))







# if 1 == 3:
#     print("Hello")
# elif 2 == 2:
#     print("Bye")