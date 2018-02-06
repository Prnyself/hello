class Robot:
    '''用于生成机器人'''
    population = 0  # 类变量，用于存储机器人的个数

    def __init__(self, name):
        '''初始化数据'''
        self.name = name
        print("initializing robot:", name)

        Robot.population += 1  # 有机器人创建时，个数加一

    def die(self):
        '''机器人死去'''
        print("robot {} is destroyed".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} is the last one".format(self.name))
        else:
            print("There is still {:d} robots working".format(Robot.population))

    def say_hi(self):
        '''机器人的问候'''
        print("hi, this is", self.name)

    @classmethod
    def how_many(cls):
        '''打印当前还剩下多少机器人'''
        print("we have {:d} robots left".format(Robot.population))


robot1 = Robot('aaa')
robot1.say_hi()
Robot.how_many()
robot2 = Robot('bbb')
robot2.say_hi()
Robot.how_many()

print("\nrobots doing sth here\n")

print("all works are done, now destroy them\n")

robot1.die()
robot2.die()

Robot.how_many()

