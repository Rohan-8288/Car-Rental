class Host:
    def __init__(self,id,carName,CarNo,price):
        self.id=id
        self.carName=carName
        self.carNo=CarNo
        self.price=price

    def __str__(self):
        data=self.id+","+self.carName+","+self.carNo+","+self.price
        return data
    
def hostCar():
    id=input("Enter a id of car: ")
    name=input("Enter Brand and Model of car: ")
    num=input("Enter Number of car: ")
    price=input("Enter per day price for car: ")

    h1=Host(id,name,num,price)

    with open("cars.txt","a") as fp:
        fp.write("\n"+str(h1).strip())
    
    print()
    print("Your Vehicle Hosted Succesfully.")
    print("Thank You for Chosing RJ SelfDrive.")