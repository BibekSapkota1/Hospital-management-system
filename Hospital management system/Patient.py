from person import Person

class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode,symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        self.__p_first_name = first_name
        self.__p_surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms=symptoms
       

    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return f"{self.__p_first_name}  {self.__p_surname}"

    def get_surname(self):
        return self.__p_surname

    def get_doctor(self) :
        #ToDo3
         return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        symptoms = input("Please enter your symptoms: ") 
        print(symptoms)

    def get_symptoms(self):
        return self.__symptoms


    def write_patientsfile(lst):
        try:
            with open("patients.txt", 'w') as fd:  # Use forward slash (/) for the file path
                fd.write('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode|    Symptoms \n')
                for index, c in enumerate(lst):
                    fd.write(f"{index+1:3}|{c.full_name():^30}|{c.get_doctor():^30}|{c.__age:^5}|{c.__mobile:^15}|{c.__postcode:^10}|{', '.join(c.__symptoms):^20} \n")
        except:
            return False
        else:
            return True
        
    def __str__(self):
        symptoms_str = ', '.join(self.__symptoms)  # Convert list to a comma-separated string
        return (f"{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{symptoms_str:^20}")