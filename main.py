import bac
import hac
import rac

if __name__ == "__main__":
    print()
    print("Welcome To RJ SelfDrive")
    print()
    print("1.Book A Car")
    print("2.Host A Car")
    print("3.Return A Car")
    print("4.Exit")

    def Bac():
        bac.book()

    def Hac():
        hac.hostCar()

    def Rac():
        rac.returnCar()
    
    choice=0
    while(True):
        choice=int(input("Please Select your option: "))
        print()
        if choice == 1:
            Bac()
            break
        elif choice == 2:
            Hac()
            break
        elif choice == 3:
            Rac()
            break
        elif choice == 4:
            break
        else:
            print("Invalid Choice !!")
