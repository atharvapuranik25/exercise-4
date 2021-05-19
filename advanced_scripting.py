names = []
admission_ID = []
CAP_rank = []
# creating three empty lists

n = int(input("Enter number of entries: "))

for i in range (0, n):
    name = input("Enter Name: ")
    a_ID = input("Enter Admission ID: ")
    cap_rank = input("Enter CAP Rank: ")

    names.append(name)
    admission_ID.append(a_ID)
    CAP_rank.append(cap_rank)

# adding user inputs to the lists

for i in range (0,n):

    message = "Hi {0[0]},\n\n Congratulations...!  You got selected for next round of recruitment process. \n Submit your academic credential including primary and secondary certificates. \n Your admission ID is {1[0]} and will be eligible for the next round of interview with a CAP rank of {2[0]}. \n If you submit all the documents on time and process university might offer you a scholarship. \n\n"
    print(message.format(names, admission_ID, CAP_rank))
    # printing the message by formatting the 0th element of each list

    names.pop(0)
    admission_ID.pop(0)
    CAP_rank.pop(0)
    # removing the 0th element of each list
    # after each loop the 1st element will become the 0th element
