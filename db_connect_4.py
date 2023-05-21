def create_db(cursor,dataBaseName):
    db=f"create database {dataBaseName}"
    cursor.execute(db)

def create_table(cursor, tb_name):
    tb1=f"CREATE TABLE IF NOT EXISTS {tb_name} (client_name varchar(200), contact varchar(50), Service_Enquired varchar(300), Location varchar(100), Building_Apartment_Name varchar(200), Date_of_Enquiry varchar(200), Estimated_Quote varchar(200), Invoice_Amount varchar(200), Profit varchar(100));"
    cursor.execute(tb1)

def insert_table(cursor,tb_name,lst):
    insert_query = f"INSERT INTO {tb_name}(client_name, contact, Service_Enquired, Location, Building_Apartment_Name, Date_of_Enquiry, Estimated_Quote, Invoice_Amount, Profit) VALUES (%(client_name)s, %(contact)s, %(Service_Enquired)s, %(Location)s, %(Building_Apartment_Name)s, %(Date_of_Enquiry)s, %(Estimated_Quote)s, %(Invoice_Amount)s, %(Profit)s);"
    cursor.executemany(insert_query,lst)

def insert_table(cursor,tb_name,lst):
    insert_query = f"UPDATE {tb_name}(client_name, contact, Service_Enquired, Location, Building_Apartment_Name, Date_of_Enquiry, Estimated_Quote, Invoice_Amount, Profit) VALUES (%(client_name)s, %(contact)s, %(Service_Enquired)s, %(Location)s, %(Building_Apartment_Name)s, %(Date_of_Enquiry)s, %(Estimated_Quote)s, %(Invoice_Amount)s, %(Profit)s);"
    cursor.executemany(insert_query,lst)