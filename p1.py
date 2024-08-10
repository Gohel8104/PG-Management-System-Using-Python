class Apna_PG:
    def _init_(self):
        self.rooms = {"Room_No":[],"Names":[],"Category":[]}
        

    def add_rooms(self):
        number_room=int(input("enter number of rooms you want to add  :  "))
        i=0
        while i<number_room:
            Room_No=[]
            Names=[]
            Category=[]
            room_number=input("enter room number :  ")
            sharing=int(input("enter sharing number for room and 0 for single :  "))
            ac_nonac=input("AC/Non-AC available in this room   ")
            Room_No.append(room_number)
            Category.append(ac_nonac)
            i=i+1
            for j in range(sharing):
                name="None"+str(j)
                Names.append(name)
            self.rooms["Room_No"].append(Room_No)
            self.rooms["Names"].append(Names)
            self.rooms["Category"].append(Category)
        self.print_data_to_txtf()

    
    def remove_room(self):
        room_number = input("enter room number for remove :  ")
        availability=self.validate_room_number()
        if room_number in availability["Roomno"]:
         a=False
        else:
         a= True
        if  a==True:
         if room_number in [room[0] for room in self.rooms["Room_No"]]:
          index = [room[0] for room in self.rooms["Room_No"]].index(room_number)
          for name in self.rooms["Names"][index]:
            if name != "None":
                del self.rooms["Names"][index]
                del self.rooms["Category"][index]
                break  # Exit loop after first non-"None" name
          del self.rooms["Room_No"][index]
          print(f"Room {room_number} removed successfully.")
         else:
          print("Room not found.")  
        else:
           print("entered room number if occupied ")

    def print_data_to_txtf(self):
        with open("apna_pg_data.txt", "a") as f:
            for i in range(len(self.rooms["Room_No"])):
                f.write(f"Room Number: {self.rooms['Room_No'][i][0]}\n")
                f.write(f"Category: {self.rooms['Category'][i][0]}\n")
                f.write("Names: ")
                for name in self.rooms["Names"][i]:
                    f.write(name + " ")
                f.write("\n\n")
        f.close()       
     
    def print_data_to_txt(self):
     with open("apna_pg_data.txt", "w") as f:
        for i in range(len(self.rooms["Room_No"])):
            f.write(f"Room Number: {self.rooms['Room_No'][i]}\n")
            f.write(f"Category: {self.rooms['Category'][i]}\n")
            f.write("Names: ")
            for name in self.rooms["Names"][i]:
                f.write(name + " ")
            f.write("\n\n")


    def read_data_from_txt(self):
        room_data = {"Room_No": [], "Category": [], "Names": []}
        with open("apna_pg_data.txt", "r") as file:
         for line in file:
          parts = line.split(":", 1)
        
          if len(parts) == 2:
            key, value = map(str.strip, parts)
            if key == "Room Number":
             room_data["Room_No"].append(value)
            elif key == "Category":
             room_data["Category"].append(value)
            elif key == "Names":
            # Split names by space and append to the list
             names = value.split()
             room_data["Names"].append(names)
        print(room_data)
        return room_data

        
       
    def validate_room_number(self, room_number):
        with open("apna_pg_data.txt", "r") as f:
            for line in f:
                if line.startswith("Room Number:"):
                    existing_room_number = line.split(":")[1].strip()
                    if room_number == existing_room_number:
                        print("hai")
                        f.close()
                        return True
        f.close()            
        print("no")            
        return False   
    

    def add_member_details(self):
     first_name = input("Enter first name: ")
     last_name = input("Enter last name: ")
     guardian_name = input("Enter guardian name: ")
     phone_number = input("Enter phone number: ")
     guardian_phone_number = input("Enter guardian phone number: ")
     college_or_work = input("Enter college/work: ")
     native_place=input("enter your naive place: ")
     joining_date=input("enter  the date of joining: ")
     expiration_date=input("enter  the date of expiration: ")
     a=self.Payment_verification(first_name)
     if a:
      filename = f"{first_name}_{phone_number[-2:]}_details.txt"
      with open(filename, "a") as file:
        file.write("|------------------------------------------------------------------------------------------------------|\n")
        file.write("|         Member Details:\n")
        file.write(f"|         First Name: {first_name}")
        file.write(f"|         Last Name: {last_name}\n")
        file.write(f"|         Guardian Name: {guardian_name}\n")
        file.write(f"|         Phone Number: {phone_number}")
        file.write(f"|         Guardian Phone Number: {guardian_phone_number}\n")
        file.write(f"|         College/Work: {college_or_work}\n")
        file.write(f"|         Native Place: {native_place}\n")
        file.write(f"|         Joining Date: {joining_date}\n")
        file.write(f"|         expiration Date: {expiration_date}\n")
        file.write("|------------------------------------------------------------------------------------------------------|\n")
      print(f"Member details saved to '{filename}'")
 
    def Payment_verification(self,firstname):
        availablity=self.check_room_availability()
        print(availablity)
        print("5 sharing and more contain smae price (6000) and after 1 sharing less 600 more  will be added.")
        rno=input("enter room number : ")
        flattened_room_numbers = [room for sublist in availablity["Roomno"] for room in sublist]
        flattened_categories = [category for sublist in availablity["Category"] for category in sublist]
        index = flattened_room_numbers.index(rno)
        data = flattened_categories[index]
        # index = availablity["Roomno"].index(rno)
        # data = availablity["Category"][index]
        print(data)
        if data=="0sharing":
           price=9000
        elif data=="1sharing":
           price=8400
        elif data=="2sharing":
           price=7800
        elif data=="3sharing":
           price=7200
        elif data=="4sharing":
           price=6600
        else:
           price=6000
        print(f"payable amount if {price}")
        Payment=int(input("Please Enter The Amount  :"))
        if Payment==price:
        #    rno=input("enter room number : ")
           self.add_name(firstname,rno)
           return True
        else:
           print("Payment failed: ")
           return False

    def check_room_availability(self):
        a=0
        availablity={"Roomno":[],"Category":[]}
        with open("apna_pg_data.txt", "r") as f:
            rno=[]
            sharing=[]

            for line in f:
                if line.startswith("Room Number:"):
                 existing_room_number = line.split(":")[1].strip() 
                  
                elif line.startswith("Names:"):
                    names_line = line.split(":")[1].strip()
                    sharing_detaill = names_line.split()  
                    for i in range(len(sharing_detaill)): 
                     Name="None"+str(i)
                     if Name ==sharing_detaill[i]:
                        print(sharing_detaill[i])
                        if i==(len(sharing_detaill)-1):
                           shar=str(len(sharing_detaill))+"sharing"
                           sharing.append(shar)
                           rno.append(existing_room_number)
        
        availablity["Roomno"].append(rno)
        availablity["Category"].append(sharing)
        return availablity

    def add_name(self, firstname, roomnumber):
     room_data = self.read_data_from_txt()
     print(room_data)
     if self.validate_room_number(roomnumber):
        index = room_data["Room_No"].index(roomnumber)
        data=room_data["Names"][index]
        print(data)
        for i in range(len(data)):
            n="None"+str(i)
            if data[i]==n:
                room_data["Names"][index][i] = firstname
                break  # Exit the loop after updating the first occurrence
        print(room_data)
        self.rooms = room_data
        self.print_data_to_txt()       
     else:
        print("Room number not found.")

    def Change_Room(self):
       name=input("enter your name : ")
       r_no=input("enter room number : ")
       room_data=self.read_data_from_txt()
       a=""
       if self.validate_name_by_room_number(name,r_no):
        self.check_room_availability()
        n_r_no=input("enter your new room nnumber : ")
        if self.check_room_availability(n_r_no):
         index =room_data["Room_No"].index(r_no)
         a=room_data["Names"][index].index(name)
         name1="None"+a
         self.add_name(name,r_no)
         self.add_name(name,n_r_no)
        else:
           print("entered valid number ")  
 

    def validate_name_by_room_number(self, name_to_validate, room_number):
     try:
        index = self.rooms["Room_No"].index(room_number)
        if self.rooms["Names"][index] == name_to_validate:
            return True
        else:
            return False
     except ValueError:
         # If room number is not found, return False
        return False    

    def remove_guest(self):
     name=input("Enter guest name to be removed :")
     rno=input("Enter Room Number of Guest :")
     room_data = self.read_data_from_txt()
     print(room_data)
     if self.validate_room_number(rno):
        index = room_data["Room_No"].index(rno)
        data=room_data["Names"][index]
        print(data)
        for i in range(len(data)):
            n=name
            na="None"+str(i)
            if data[i]==n:
                room_data["Names"][index][i] = na
                break  # Exit the loop after updating the first occurrence
        print(room_data)
        self.rooms = room_data
        self.print_data_to_txt()       
     else:
        print("Room number not found.")
         
a=Apna_PG()
c=True
while c:
     print("enter 1 for add Rooms")
     print("enter 2 for remove room ")
     print("enter 3 for  display all rooms details")
     print("Enter 4 to add guest")
     print("enter 5 for remove guest")
     choice=int(input("enter your choice or 0 for exit :  "))
     if choice==1:
       a.add_rooms()
     if choice==2:
        a.remove_room()
     if choice==3:
        a.read_data_from_txt()          
     if choice==4:
        a.add_member_details()
     if choice==5:
        a.remove_guest()
     if choice==0:
        c=False
     else:
        print("enter valid choice :  ")