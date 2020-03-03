''' CREATING TABLES'''

# with connection.cursor() as cs:
#     sql_cmd = f'create table devices (id int(3) AUTO_INCREMENT PRIMARY KEY NOT NULL, name varchar(30))'

#     cs.execute(sql_cmd)
#     connection.commit()

# ''' CREATE DATA TABLE '''

# with connection.cursor() as cs:
#     sql_cmd = f'create table data (device_id int AUTO_INCREMENT NOT NULL, FOREIGN KEY (device_id) REFERENCES devices(id), id int(11), status int, time varchar(30))'

#     cs.execute(sql_cmd)
#     connection.commit()
