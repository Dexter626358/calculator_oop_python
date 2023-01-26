import Checker
from Complex1 import Complex1
import ComplexParser
from Real import Real


class UserInterface:
    def menu(self):
        print("Калькулятор умеет выполнять операции над действительными и комплексными числами")
        print("Введите операцию:\n 1. Сложение.\n 2. Вычитание.\n 3. Умножение.\n 4. Деление.\n 5. Выход.")

    def user_choose(self):
        flag = True
        while flag:
            print("Введите числа через пробел: ")
            numbers = list(map(str, input().split(" ")))
            number1 = numbers[0]
            number2 = numbers[1]
            self.menu()
            operation = input()
            if operation == "1":
                if number1.isdigit() and number2.isdigit():
                    print(Real(float(number1), float(number2)).__add__())
                elif Checker.iscomplex(number1) and Checker.iscomplex(number2):
                    comp1 = sep_complex(number1)
                    comp2 = sep_complex(number2)
                    print(comp1 + comp2)
                else:
                    print("С таким числами я не умею производить вычисления")

            elif operation == "2":
                if number1.isdigit() and number2.isdigit():
                    print(Real(float(number1), float(number2)).__sub__())
                elif Checker.iscomplex(number1) and Checker.iscomplex(number2):
                    comp1 = sep_complex(number1)
                    comp2 = sep_complex(number2)
                    print(comp1 - comp2)
                else:
                    print("С таким числами я не умею производить вычисления")
            elif operation == "3":
                if number1.isdigit() and number2.isdigit():
                    print(Real(float(number1), float(number2)).__mul__())
                elif Checker.iscomplex(number1) and Checker.iscomplex(number2):
                    comp1 = sep_complex(number1)
                    comp2 = sep_complex(number2)
                    print(comp1 * comp2)
                else:
                    print("С таким числами я не умею производить вычисления")
            elif operation == "4":
                if number1.isdigit() and number2.isdigit():
                    print(Real(float(number1), float(number2)).__truediv__())
                elif Checker.iscomplex(number1) and Checker.iscomplex(number2):
                    comp1 = sep_complex(number1)
                    comp2 = sep_complex(number2)
                    print(comp1 / comp2)
                else:
                    print("С таким числами я не умею производить вычисления")
            elif operation == "5":
                break
            else:
                print("Такой операции не существут")



def sep_complex(number1):
    number1_lst = ComplexParser.complexsplit(number1)
    comp = Complex1(number1_lst[0], number1_lst[1])
    return comp