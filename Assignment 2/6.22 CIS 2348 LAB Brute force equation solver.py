#Mustafa Eski
#PSID: 2046388
# 6.22 CIS 2348 LAB: Brute force equation solver

num_a = int(input())
num_b = int(input())
num_c = int(input())
num_d = int(input())
num_e = int(input())
num_f = int(input())

solution = False #(Reference = https://stackoverflow.com/questions/62271257/solving-a-system-of-equations-by-brute-force-within-a-given-range-without-sympy)
for x in range(-10,11):
    for y in range (-10,11):
        if num_a * x + num_b * y == num_c and num_d * x + num_e * y == num_f:
            solution = True
            print (x,y)
if solution  == False:
    print('No solution')


