import json
path = "C:/Users/MY PC/Desktop/Prog_python/acct_db.json"
# file = open(path, newline = "")
# reader = csv.reader(file)

with open("acct_db.json") as fobj:
    details = fobj.read()
print(details)
# header = next(reader)
# data = [row for row in header]

# print(header)
# print(data[0])