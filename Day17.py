# Introduction to OOPS continued...

# class Emp:
#     # properties / attributes
#     empId = 1234
#     empRole = "Developer"
#     empCTC = "20LPA"

#     # methods
#     # self - this keyword -->> refers current object 
#     def PersonalDetails(self):
#         print("Methods")

# # instance/object
# emp1 = Emp()
# print(emp1.empId)
# print(emp1.empRole)
# print(emp1.empCTC)

# emp1.PersonalDetails()

# =====================================================

# Constructor
# -Constructor is used to initialize the properties/ variables of class
# -Constructor is Automayically get called when instance get created.

#  __init__ - constrcutor is a special type of methods or fucntion which is used to intialize or set instanceof a class 
# automatically invoked
# used to defined common class properties/attributes

# ========================================

# self >
# -self refers/creates the variables for each object
# self refer the current object of a class

# ====================================

# class Variable - Accessible everywhere 
# class Company:
#     company_name = "TCS" # class Variable 

#     def Dept(self,dept_name, dept_id):
#         self.dept_name=dept_name
#         self.dept_id=dept_id

#         print("Company name Is : ", self.company_name)
#         print("Company Department Details :  ",self.dept_name,"  ", self.dept_id)

# c1 = Company()
# print(c1.company_name)
# d1=c1.Dept("IT",123)

# ====================================

class Car:
    car_brand="Honda"

    def __init__(self,name,color,model):
        
        # instance variables
        self.name=name
        self.color=color
        self.model=model
        print(f"Car Details. {self.name} and {self.color} {self.model} and Company Brand. {self.car_brand}" )

    def start(self):
        print(f"{self.name} Car Start....")
    


c1=Car("Honda CIvic","Black","S+")
c2=Car("Hyundai Verna","White","S+")
c3=Car("Hyundai Creata","Black","S")

c3.start()

