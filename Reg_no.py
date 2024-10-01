class Registration:
    def __init__(self, Name, RegNo):
        self.Name = Name
        self.RegNo = RegNo

    def show_info(self):
        print(f"RegNo: {self.RegNo}")
        print(f"Name: {self.Name}")    

student1 = Registration("Ademba", "M23B13/015")
student2 = Registration("Musinguzi", "S23B13/016")
student3 = Registration("Wobuteyi", "M23B13/018")



print(student1.show_info())
print(student2.show_info())
print(student3.show_info())
