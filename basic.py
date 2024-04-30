# class Phone:
#     def make_call(self):
#         print("making call")
#     def play_game(self):
#         print("playing game")
# p1=Phone()
# p1.make_call()
# p1.play_game()

# class Phone:
#     def set_color(self,color):
#         self.color=color
#     def set_cost(self,cost):
#         self.cost=cost
#     def show_color(self):
#         return self.color
#     def show_cost(self):
#         return self.cost
# p2=Phone()
# p2.set_color("Blue")
# p2.set_cost(30000)
# print("color",p2.show_color)
# print(p2.show_cost)




class employee:
    # consturctor
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def employee_detaills(self):
        print("name of employee",self.name)
        print("age of employee",self.age)
        print("salary of employee", self.salary)
        print("gender of employe",self.gender)
e1=employee("Ram",23,25000,"male")
e1.employee_detaills()

