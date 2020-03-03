import statistics

class Table:

    def __init__(self, filename):

        self.filename  = filename

        col_data = self.get_col_names()
        row_data = self.get_num_rows()

        self.col_names = col_data[1]
        self.col_count = col_data[0]
        self.row_count = row_data

    def __get_raw_data(self):

        lines = open(self.filename, "r").readlines()
        lines.pop(0)

        list_of_tuples = map(lambda string: string.split(","), lines)

        unzipped_data = list(zip(*list_of_tuples))

        return unzipped_data


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

        unzipped_data = self.__get_raw_data()

        text_col = []
        num_col = []
        count = 0

        for line in unzipped_data:
            
            if all(map(lambda x: x.replace(".", "").isdigit(), line)):
                num_col.append(self.col_names[count])
            else:
                text_col.append(self.col_names[count])

            
            count += 1

        return (text_col, num_col)

        # print(text_col)
        # print(num_col)

    def get_col(self, col_name):

        try:

            unzipped_data = self.__get_raw_data()
            cols = self.col_names

            selected_col_index = cols.index(col_name)
            data = unzipped_data[selected_col_index]
            # print(data)

            return data

        except ValueError:

            print("SORRY NO SUCH INDEX IN FILE")
            return []


    def stats(self):
        numeric_cols = self.get_numeric_cols()[1]
        
        for col in numeric_cols:
            print(f"{col}")

            
            col_data = self.get_col(col)
            col_to_int = list(map(lambda x : float(x), col_data))

            mean = statistics.mean(col_to_int)
            min_val = min(col_to_int)
            max_val = max(col_to_int)

            print(f"\tmean - {mean}")
            print(f"\tmin_val - {min_val}")
            print(f"\tmax_val - {max_val}")
        print
            

new_data = Table("c:/Users/INYANG/Desktop/PERSONAL WORK/PYTHON_CLASS/datapackages/paylater/application_data.csv")
print(new_data.filename)
new_data.col_names
print(new_data.row_count)
new_data.get_numeric_cols()
new_data.get_col("ICE CREAM")
new_data.stats()

# file = open("DNMM_CDD_18C.csv", "r")
# print(len(file.readlines())-1)

# print("GH73053338".isdigit())