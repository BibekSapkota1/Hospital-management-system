from Doctor import Doctor
from Patient import Patient


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        if(self.__username == username) & (self.__password == password):
            return True
        else:
            return False

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        doctor_firstname = input("Enter the first name of the doctor: ")
        doctor_surname = input("Enter the surname of the doctor: ")
        doctor_speciality = input("Enter the speciality of the doctor: ")

        return doctor_firstname,doctor_surname,doctor_speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input("Please input the operation: ")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            doctor_firstname, doctor_surname, doctor_speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if doctor_firstname == doctor.get_first_name() and doctor_surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists=True
                    break
                
                    
                    #ToDo6
                else:
                    name_exists=False
            if(name_exists!=True):
                doctors.append(Doctor(doctor_firstname,doctor_surname,doctor_speciality))
                print('Doctor registered.') # save time and end the loop

            

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            #ToDo8
            if(op == 1):
                new_firstname = input("Enter the new first name : ")
                doctors[index].set_first_name(new_firstname)
                print("Your first name is updated.")
                
            elif(op == 2):
                new_surname = input("Enter the new surname : ")
                doctors[index].set_surname(new_surname)
                print("Your surname is updated.")
                
            elif(op == 3):
                new_spec = input("Enter the new speciality : ")
                doctors[index].set_speciality(new_spec)
                print("Your speciality is updated.")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
            #ToDo9
            doctor_exits=self.find_index(doctor_index,doctors)
            if(doctor_exits!=False):
                del doctors[doctor_index]
                print("Doctor deleted")
            else:
                print("ID Not Found.")
           
           

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |   Symptoms')
        #ToDo10
        for index, item in enumerate(patients):
            print(f'{index+1:3}|{item}')

    def read_patientsfile(read_data_files):
        patient_list = []
        try:
            with open(read_data_files, 'r') as d:
                for i in  d:
                    print(i.split(','))
                    patient_list.append(i)

        except FileNotFoundError:
            print(" No file found")

        finally:
            return patient_list
        
    

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |   Symptoms')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name()) 
                self.view(patients)
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                # self.write_patientsfile(doctors)
                print('The patient is now assign to the doctor.')

                if Patient.write_patientsfile(patients):
                    print("Patient records successfully updated in patients file")
                else:
                    print("Failed to update records in patient file")

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        #ToDo12
        self.view(patients)
        try:
            if (len(patients)!=0):
                patient_index=int(input('please enter the patients ID: '))-1
                discharge_patients.append(patients[patient_index])
                del patients[patient_index]                                            # -----------------------------------------------------------------
                print("Patient Sucessfully discharged. \n") 

            else:
                print("Not able to discharge.")

        except IndexError: 
            print('The id entered is incorrect')
            return 
            
        

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |   Symptoms')
        #ToDo13
        self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            username1 = input('Enter the new username: ')
            # validate the username
            username2 = input('Enter the new username again: ')
            if(username1 == username2):
                print("Username matched.")
                self.__username = username2
                print("------------------------------")
                print("-----------Username updated !!! -------------")
            else:
                print("Username not matched")   

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print("----------------Password updated !!!---------------")
            else:
                print("Password not matched") 

        elif op == 3:
            address = input('Enter the new address: ')
            # validate the address
            if address == input('Enter the new address again: '):
                self.__address = address
                print("------------- Address updated !!! -------------")
            else:
                print("Address not matched") 

        else:
            #ToDo16
            print("Invalid Choice.")


    def doctor_relocate(self,patients,doctors):

        print('Select the doctor that you need to relocate:')
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)

        try:
            doctor_index = input('Please enter the doctor ID to relocate: ')
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:

                print('The entered ID is found')

                

            # if the id is not in the list of doctors
            else:
                print('The entered Id is not found')

        except ValueError: # the entered id could not be changed into an in
            print('Invalid ID')


        print("-----Relocate-----")
        self.view(patients)

        try:
            patient_index = input('Please enter the patient ID to relocate doctor: ')


            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index in range(len(patients)):
                patients[patient_index].link(doctors[doctor_index].full_name()) 
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                if Patient.write_patientsfile(patients):
                    print("Patient records successfully updated in patients file")
                else:
                    print("Failed to update records in patient file")

                print("Sucessfully Rellocated !")
            else:
                print('ID not found')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('Incorrect ID')


    def get_management_report(self,doctors,patients):
        print("------Management Reports-------")
        print('Choose the operation:')
        print(' 1- Total number of doctors in the system')
        print(' 2- Total number of patients per doctor')
        print(' 3 - Total number of appointments per month per doctor')
        print('4 - Total number of patients based on the illness type.')
        b = input('Choose an option: ')
        try:
            if b =='1':
                a=len(doctors)
                print(f" total number of doctors: {a}")

            elif b =='2':
                for i in doctors:
                    totalPatients = i.get_total_patients()
                    print(f"{i.full_name()} has {totalPatients} patients")
            
            
            elif b =='3':
                for i in doctors:
                    total_appointment = i.get_total_appointment()
                    print(f"{i.full_name()} consists {total_appointment} this month")

            
            elif b =='4':

                for i in patients:
                    symptoms = i.get_symptoms()
                    t=0
                    for p in patients:
                        if p.get_symptoms() == symptoms:
                            t+=1
                    print(f'{t} for {symptoms}')

            else:
                print("Invalid Option")

        except Exception as x:
            print(x)

    def print_patients_of_same_family(self, patients):
        family_name = input("Enter the family name: ")
        family_patients = []

        for patient in patients:
            if patient._Patient__p_surname.lower() == family_name.lower():
                family_patients.append(patient)

        if len(family_patients) > 0:
            print("Patients of the same family:")

            self.view(family_patients)
        else:
            print("No patients found from the specified family.")
