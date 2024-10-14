class Bird:
    def __init__(self):
        print("Bird is ready")
    def who_is_this(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def who_is_this(self):
       print("Penguin")
    def run(self):
        print("Run faster")
penguin1=Penguin()
penguin1.who_is_this()
penguin1.swim()
penguin1.run()