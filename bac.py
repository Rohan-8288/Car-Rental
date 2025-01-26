class Bac:
    def displayCars(self):
        with open("cars.txt","r") as fp:
            deatails=fp.readlines()
            for car in deatails:
                print(car)
            print()
        
    def remove_line_from_file(self,file_name, line_to_remove):
        with open(file_name, "r") as file:
            lines = file.readlines()

        with open(file_name, "w") as file:
            for line in lines:
                if line.strip() != line_to_remove.strip():
                    file.write(line)

    def confirmCar(self,a):
        print("Car You Want to Book is:",a[1])
        print("Per day Charges Of This Car is:",a[3])
        days=input("Please tell for How many days you want to book a car: ")

        with open("days.txt","a") as fp:
            data=",".join(a)
            fp.write(data.strip()+","+days.strip()+"\n")

        with open("booked.txt","a") as fp:
            fp.write(data.strip()+"\n")

        print("Your Bokking For Car",a[1],"is Confirmed..")
        print("Have Safe Journey !")
        print("Note:-Make payment at the time of returning a Car.")
        self.remove_line_from_file("cars.txt",data)
        

    def carBook(self):
        choice=input("Which Car You Want To Rent: ")

        with open("cars.txt","r") as fp:
            deatails=fp.readlines()
            for car in deatails:
                a=car.split(",")
                if choice == a[0].strip():
                    self.confirmCar(a)
                    return
            print("Car not found. Please check the ID and try again.")
                    




def book():
    b1=Bac()
    b1.displayCars()
    b1.carBook()

# b1=Bac()
# b1.displayCars()
# b1.carBook()

