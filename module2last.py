def password(number):
    right_password = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                right_password += str(i) + str(j)
    return right_password

print('Введите число: ')
print(password(int(input())))