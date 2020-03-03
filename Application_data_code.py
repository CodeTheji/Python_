import csv


path = "C:/Users/MY PC/Desktop/Prog_python/application_data.csv"
file = open(path)
data = file.readlines()
print(data[0])

class Application_data:

     def __init__(self, names_of_columns):
        Application_data.__init__(self, names_of_columns)
        self.data = column_1

        names_of_columns = self.data.replace(",", "")
column_1 = Application_data(data = data[0])

print(names_of_columns)
print(column_1)

# lines = [line for lines in open(path)]

# print(line[0])
# # for line in file:
# #     print(line)