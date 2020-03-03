import statistics




class Table:

    def __init__(self, filename):

        self.filename  = filename

        col_data = self.get_col_names()
        row_data = self.get_num_rows()

        self.col_names = col_data[1]
        self.col_count = col_data[0]
        self.row_count = row_data


    def get_col_names(self):

        col_row = open(self.filename, "r").readlines()[0]
        col_names = col_row.split(",")

        print("COLUMNS IN FILE : ")
        for name in (col_names):
            print(f"\t{name}")

        num_of_cols = len(col_names)
        
        return num_of_cols, col_names

    def get_num_rows(self):

        num_rows = len(open(self.filename, "r").readlines())-1

        return num_rows

    def get_numeric_cols(self):

        lines = open(self.filename, "r").readlines()
        lines.pop(0)

        list_of_tuples = map(lambda string: string.split(","), lines)

        unzipped_data = zip(*list_of_tuples)

        text_col = []
        num_col = []
        count = 0

        for line in unzipped_data:
            
            if not any(map(lambda x: x.replace(".", "").isnumeric(), line)):
                num_col.append(self.col_names[count])
            else:
                text_col.append(self.col_names[count])

            count += 1

        # print(text_col)
        # print(num_col)
            

# new_data = Table("DNMM_CDD_18C.csv") #this one and the remaining under..making 5 are for the top solutions
# print(new_data.filename)
# new_data.col_names
# print(new_data.row_count)
# new_data.get_numeric_cols()

# file = open("DNMM_CDD_18C.csv", "r")
# print(len(file.readlines())-1)


    def getmin_value(self):

        lines = open(self.filename, "r").readlines()
        lines.pop(0)


        list_of_tuples = map(lambda string: string.split(","), lines)

        unzipped_data = zip(*list_of_tuples)

        min_value = []
        max_value = []
        mean_value = []

        for line in unzipped_data:

            if not any(map(lambda x: x.replace(".", "").isnumeric(), line)):
                pass
            else:
                min_value = min(line)
                min_values.append(min_value)
                max_value = max(line)
                max_values.append(max_val)
                mean_value = statistics.mean(line)
                mean_values = append(mean_value)

        print(min_values)
        print(max_values)
        print(mean_values)
