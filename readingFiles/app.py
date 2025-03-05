employee_file = open("employees.txt","r")

#print(employee_file.read())
#print(employee_file.readline()) # ilk satırı okur diğer satıra geçer tekrar aynı fonskiyonu çağırısan sıradaki satırı okur
#print(employee_file.readline())

#print(employee_file.readlines())
#print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)
employee_file.close()
