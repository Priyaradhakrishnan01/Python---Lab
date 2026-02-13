


class Student:
    def getStudentDetails(self):
        self.rollno = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
        self.physics = int(input("Enter Physics Marks: "))
        self.chemistry = int(input("Enter Chemistry Marks: "))
        self.maths = int(input("Enter Math Marks: "))


class SDetails(Student):
    def printResult(self):
        self.percentage = (self.physics + self.chemistry + self.maths) / 300 * 100
        print(f"Roll No: {self.rollno}, Name: {self.name}, Percentage: {self.percentage:.2f}%")


class GraceMarks(SDetails):
    def addGraceMarks(self):
        if self.percentage > 70:
            self.physics += 9  
            print("Grace marks added to Physics.")
        else:
            print("No grace marks, percentage is below 70.")
    
    def printResultAfterGrace(self):
        self.addGraceMarks()
        print("Result after adding grace marks:")
        self.printResult()


S1 = GraceMarks()
S1.getStudentDetails()
print("Result:")
S1.printResult()  
S1.printResultAfterGrace()  
