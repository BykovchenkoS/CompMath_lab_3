import math


def trapezoidal_rule(function, a, b, n=1000, epsilon=1e-6, method='mean'):
    try:
        if math.isinf(a) or math.isinf(b) or math.isnan(a) or math.isnan(b):
            raise ValueError("И a, и b должны быть конечными.")

        if not isinstance(n, int) or n <= 0:
            raise ValueError("N должно быть целым числом, большим нуля.")

        if not isinstance(epsilon, float) or epsilon <= 0:
            raise ValueError("Эпсилон должен быть положительным с плавающей запятой.")

        if math.isinf(function(a)) or math.isnan(function(a)):
            if math.isinf(function(b)) or math.isnan(function(b)):
                raise ValueError("Функция имеет устарняемые разрывы в обоих пределах интегрирования.")
            else:
                print("Функция имеет устраняемый разрыв на нижнем пределе интегрирования.")
                if method == 'left':
                    a += epsilon
                elif method == 'right':
                    a -= epsilon
                elif method == 'mean':
                    a = (function(a + epsilon) + function(a - epsilon)) / 2
                else:
                    raise ValueError("Недопустимый вариант. Допустимыми вариантами являются 'left', 'right', or 'mean'.")

        elif math.isinf(function(b)) or math.isnan(function(b)):
            print("Функция имеет устраняемый разрыв на верхнем пределе интегрирования.")
            if method == 'left':
                b -= epsilon
            elif method == 'right':
                b += epsilon
            elif method == 'mean':
                b = (function(b + epsilon) + function(b - epsilon)) / 2
            else:
                raise ValueError("Недопустимый вариант. Допустимыми вариантами являются 'left', 'right', or 'mean'.")

        h = (b - a) / n
        integral = 0.5 * (function(a) + function(b))

        for i in range(1, n):
            x_i = a + i * h
            integral += function(x_i)

        integral *= h

        second_derivative = (function(a + h) - 2 * function(a) + function(a - h)) / h ** 2
        error = ((b - a) * h ** 2 / 12) * abs(second_derivative)

        return integral, error

    except Exception as e:
        print("Произошла ошибка:", e)


print("Выберите функцию для интегрирования:")
print("1. sin(x)")
print("2. cos(x)")
print("3. x**2")
print("4. e**x")
print("5. sin(x)/x")

choice = input("Введите номер функции (1-5): ")
a = float(input("Введите нижний предел интегрирования: "))
b = float(input("Введите верхний предел интегрирования: "))
n = int(input("Введите количество интервалов (n): "))

if choice == "1":
    function = math.sin

elif choice == "2":
    function = math.cos

elif choice == "3":
    function = lambda x: x ** 2

elif choice == "4":
    function = lambda x: math.exp(x)

elif choice == "4":
    function = lambda x: math.exp(x)

elif choice == "5":
    function = lambda x: math.sin(x) / 2

else:
    raise ValueError("Ошибка: неверный выбор функции.")


try:
    result, error = trapezoidal_rule(function, a, b, n)
    print("Результат интегрирования:", result)
    print("Оценка погрешности:", error)
except ValueError as e:
    print("Произошла ошибка:", str(e))
except TypeError as e:
    print("Произошла ошибка:", str(e))
