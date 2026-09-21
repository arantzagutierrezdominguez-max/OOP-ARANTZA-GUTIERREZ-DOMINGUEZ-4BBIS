#Lab1. Creating a Class, Object, Attributres & Methods.
#Student: Arantza Gutierrez Dominguez Object-Oriented Programming 4·B

#In this lab you are going to explore and create a program that defines a class called backpack

class Table:
  def __init__(self, color, shape, material):
    self.color = color
    self.shape = shape
    self.material = material

  def move(self):
    print("The table is moving")

  def describe(self):
    print(f"This backpack is made with {self.material}", f"the shape of this backpack is {self.shape}", f"the color of this backpack is {self.color}")

#self: se utiliza para decirle a python a que un objeto pertenecen los atributos
#Create an instance using the class "table"
table1 = Table("brown", "Rectangular", "fabric")
table2 = Table("yellow", "circle", "wood")


#We access to the object(Intance "table 1" to call itds data)
print(table1.material)
print(table2.color)
table1.move()
table2.describe()

               #Intance "table 2"
print(table2.material)

#Lab 1:Bank Account Class
#Create a Python program that models a bank account using Object-Oriented Programming.

class BankAccount:
    def __init__(self, holder, initial_balance):
        self.holder = holder
        self.__balance = initial_balance  # El doble guion bajo (__) lo hace un atributo privado

    # 4. Método para depositar dinero
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful. New balance: ${self.__balance}")
        else:
            print("Error: The deposit amount must be greater than zero.")

    # 5. Método para retirar dinero
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: The withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Error: Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrawal successful. New balance: ${self.__balance}")

    # Método para consultar el saldo (al ser privado __balance, necesitamos un método para verlo)
    def get_balance(self):
        return self.__balance


# Crear una instancia (cuenta bancaria)
account1 = BankAccount("Ana", 500)

# Consultar titular y saldo inicial
print(f"Account holder: {account1.holder}")
print(f"Initial balance: ${account1.get_balance()}")

# Depositar dinero (Caso válido e inválido)
account1.deposit(200)   # Suma 200 -> Nuevo saldo: 700
account1.deposit(-50)   # Muestra mensaje de error

# Retirar dinero (Casos válidos e inválidos)
account1.withdraw(100)  # Resta 100 -> Nuevo saldo: 600
account1.withdraw(1000) # Muestra error de fondos insuficientes
