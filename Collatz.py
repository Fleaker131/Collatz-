#--------------------------------------------------#
# Creater By Fleaker #
# Create Date And Time : 02:24 07/06/2020 #
#--------------------------------------------------#

number = int(input("Number : "))
def collatz(n):
   while n !=1:
    if(int(n)%2==0):
        print("! Even Number !")
        n = (n // 2)
        return (print(int(n)))
    else:
        print("Odd Number !")
        n = (3 * n+1)
        return (print(int(n)))
    continue
collatz(number)
