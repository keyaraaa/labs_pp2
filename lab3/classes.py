class Stringus:
    def __init__(main, string):
        main.string = ""
    def get_string(main):
        main.string=input()
    def print_string(main):
        print(main.string)

pq = Stringus("A")
pq.get_string()
pq.print_string()

#Task2
class Shape:
    def __init__(self, area, length):
        self.length = 0
        self.area = self.length ** 2
    def parea(self):
        print(self.area)
class Square(Shape):
    def __init__(self, area, length):
        super().__init__(area, length)
        self.length = int(input())
        self.area = self.length ** 2
pq = Shape(1, 2)
pq.parea()
pq = Square(1, 2)
pq.parea()

#Task 3
class Shape:
    def __init__(self, area, length, width):
        self.length = 0
        self.width = 0
        self.area = self.length * self.width
    def parea(self):
        print(self.area)
class Square(Shape):
    def __init__(self, area, length, width):
        super().__init__(area, length, width)
        self.length = int(input())
        self.width = int(input())
        self.area = self.length * self.width
pq = Shape(1, 2, 3)
pq.parea()
pq = Square(1, 2, 3)
pq.parea()

#Task 4
class Point:
    def __init__(self, x, y, z):
        self.x = int(input())
        self.y = int(input())
        self.z = int(input())
    def show(self):
        print([self.x, self.y, self.z])
    def move(self):
        print("Enter the change for each coordinate:")
        print("For x:")
        nx = int(input())
        print("For y:")
        ny = int(input())
        print("For z:")
        nz = int(input())
        self.x+=nx
        self.y+=ny
        self.z+=nz
    def dist(self, other_point):
        print(((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 + (self.z - other_point.z) ** 2) ** 0.5)
        

a = Point(1, 2, 3)
b = Point(2, 3, 4)
a.show()
a.move()
a.show()
a.dist(b)

#Task 5
class BankAcc:
    def __init__(self, owner, balance):
        self.owner = input("Please, enter your Name:")
        self.balance = int(input("Please, insert the money:"))
        print("Account Owner:", self.owner)
        print("Account Balance:", self.balance)
    def deposit(self, amount):
        self.amount = int(input("Please, enter your deposit:"))
        if self.amount < 0:
            print("Enter real numbers.")
        else:
            self.balance+=self.amount
            print("Your new balance:", self.balance)
    def withdrawal(self, amount):
        self.amount = int(input("Please enter the amount of money you want to withdrawal:"))
        if self.amount < 0 or self.amount > self.balance:
            print("Insufficient amount of money.")
        else:
            self.balance-=self.amount
            print("Your new balance:", self.balance)
    def manipulate(self, choice):
        
        switch = True
        while switch:
            choice = input("Please, enter what would you like to do: Deposit(deposit), Withdrawal(withdrawal) or exit(exit):")
            if choice == "exit":
                print("Succesfully exited the programm.")
                break
            elif choice == "deposit":
                self.deposit(1)
            elif choice == "withdrawal":
                self.withdrawal(2)
            else:
                print("Enter one of the 3 options.")
                

a = BankAcc(1, 2)
a.manipulate(1)

#Task 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = map(int,input().split())
numbers = list(a)

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)