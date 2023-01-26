import re

"""
 * Метод проверяет представляет ли строка число
 * (целое или с плавающей запятой)
 * @param str - строка для проверки, является ли она числом (String)
 * @return - true или false в зависимости число или нет (boolean)
 """
def isnumeric(stroka):
    tpl = r'-?\\d+(\\.\\d+)?'
    if re.match(tpl, stroka):
        return True
    else:
        return False
     # проверяет число c возможным минусом и десятичной точкой

"""
 * Метод проверяет представляет ли строка ЦЕЛОЕ число
 * @param str - строка для проверки, является ли она целым числом (String)
 * @return - true или false в зависимости число или нет (boolean)
 """
def isinteger(stroka):
    tpl = r"-?\\d+"
    if re.match(tpl, stroka):
        return True
    else:
        return False  # проверяет число с возможным минусом

"""
* Метод проверяет представляет ли строка КОМПЛЕКСНОЕ число
 * @param str - строка для проверки
 * @return - true или false в зависимости число или нет (boolean)
"""

def iscomplex(stroka):
    tpl = r'^(?!$)(?P<real>(?P<sign1>[+-]?)(?P<number1>\d+(?:\.\d+)?))?(?:(?P<imag>(?P<sign2>[+-]?)(?P<number2>\d+(?:\.\d+)?j)))?$'
    if re.match(tpl, stroka):
        return True
    else:
        return False

