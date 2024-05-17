class Operations:
    def __int__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display(self):
        print("Variable 1: ", self.var1)
        print("Variable 2: ", self.var2)

    def change_vars(self, new_var1, new_var2):
        self.var1 = new_var1
        self.var2 = new_var2

    def sum_vars(self):
        return self.var1 + self.var2

    def max_var(self):
        return max(self.var1, self.var2)


def main():
    nr1 = int(input("Insert a number: "))
    nr2 = int(input("Insert another number: "))

    obj = Operations(nr1, nr2)
    obj.display()

    print("Sum of variables:", obj.sum_of_variables())
    print("Largest variable:", obj.largest_variable())

    obj.change_variables(10, 3)
    obj.display()

    print("Sum of variables:", obj.sum_of_variables())
    print("Largest variable:", obj.largest_variable())


if __name__ == '__main__':
    main()
