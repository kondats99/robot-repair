import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.head = self.connect_body_part()
        self.arms = self.connect_body_part()
        self.legs = self.connect_body_part()

    def connect_body_part(self):
        return random.random() > 0.5

    def start(self):
        
        if not self.head:
            raise Exception("Head not connected")
        
        if not self.arms:
            raise Exception("Arms not connected")
        
        if not self.legs:
            raise Exception("Legs not connected")
        
        print(f"{self.name} is up and running!")

class RepairShop:
    def __init__(self, owner):
        self.owner = owner
        self.repairs = []

    def repair_logging(self):
        print(f"{self.owner}'s shop repair list:")
        for repair in self.repairs:
            print(repair)

    def new_repair_log(self, robot_name, part_name):
        self.repairs.append({'robot name': robot_name, 'fixed part': part_name})

    def fix_robot(self, robot):
        
        if not robot.head:
            robot.head = True
            self.new_repair_log(robot.name, 'head')

        if not robot.arms:
            robot.arms = True
            self.new_repair_log(robot.name, 'arms')

        if not robot.legs:
            robot.legs = True
            self.new_repair_log(robot.name, 'legs')
        
        robot.start()    


# Example
shop = RepairShop("Smith")
robot1 = Robot("Wall-E")
robot2 = Robot("R2-D2")

shop.fix_robot(robot1)
shop.fix_robot(robot2)

print("The robots are up and running!")
shop.repair_logging()
