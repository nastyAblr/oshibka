
dict_school = {}
students = {'Johnny', 'Bilbo', 'Steven', 'Knedrik', 'Aaron'}
list_students = (sorted(list(students)))
print(list_students)
grades = [[5,3,3,5,4,], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
dict_school['Aaron'] = sum(grades[0])/len(grades[0])
dict_school['Bilbo'] = sum(grades[1])/len(grades[1])
dict_school['Johnny'] = sum(grades[2])/len(grades[2])
dict_school['Knedrik'] = sum(grades[3])/len(grades[3])
dict_school['Steven'] = sum(grades[4])/len(grades[4])
print(dict_school)


