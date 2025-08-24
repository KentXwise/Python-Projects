#Gihimo ni nga code para sa mga beginners sa Python aron makat-on unsaon paghandle ug errors gamit ang try ug except

#--------------------------------------------------------------------------------------------------#
# E-uncomment ni nga code aron makita unsaon basic paghandle ug errors
#number = input ('Please provide a number: ')
# try:
#     print(10 + int(number))
# except:
#     print("Please provide a valid number")
#--------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------#
# E-uncomment ni nga code aron makita unsaon bisag ng except na mo run gihapon ang code
while True:
    number = input('Please provide a number: ')
    try:
        print(10 + int(number))
        break   # para mo exit sa loop kung successful ang try
    except:
        print("Please provide a valid number")
#--------------------------------------------------------------------------------------------------#


