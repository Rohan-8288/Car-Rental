def remove_line_from_file(file_name, line_to_remove):
    with open(file_name, "r") as file:
        lines = file.readlines()

    with open(file_name, "w") as file:
        for line in lines:
            if line.strip() != line_to_remove.strip():
                file.write(line)

def returnCar():
    print("Welcome Back,Hope Your Journey Was Awesome !!")
    id=input("Enter id of car you booked: ")

    with open("days.txt","r") as fp:
        lines=fp.readlines()
        for line in lines:
            a=line.split(",")
            if id == a[0]:
                print("The Car you Booked is",a[1])
                print("The Car was booked for days",a[4])
                print("Charges you Have to pay are",int(a[4]) * int(a[3]))

                data=",".join(a)
                remove_line_from_file("days.txt",data)

                parts = data.split(",")
                parts.pop(4)
                result = ",".join(parts)
                remove_line_from_file("booked.txt",result)

                with open("cars.txt","a") as file:
                    file.write(result.strip())
                print("Thank You For Chossing RJ SelfDrive")
            