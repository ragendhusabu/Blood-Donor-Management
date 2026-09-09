
from mysql import connector
import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection =connector.connect(
            host = "localhost",
            user = "root",
            password ="321996",
            database ="blood_db"
        )
        print("Connected successfully..")

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor Added Successfully..!")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query ="select * from donor"
            self.cursor.execute(query)
            records =self.cursor.fetchall()
            #print(records)
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def retrieve(self,id=None): # setting default argument
        try:
           record= self.get_object(id=id)
           if record == None:
               print("Data not Found..")
           else:
               print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            records = self.get_object(id=id)
            values=(id,)
            if records != None:
                self.cursor =self.connection.cursor()
                query = "delete from donor where id= %s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor Deleted Successfully...!")
            else:
                print("Donor not Found...!")

        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id) # to find the donor with given id
            if record !=None:
                self.cursor = self.connection.cursor()
                placeholder="" # create empty string, this dynamic variable will be used to construct the set part of the SQL query
                for k in kwargs.keys():
                    placeholder += k +"=%s, "
                placeholder = placeholder.rstrip(", ") # rstrip removes last comma to work where close work properly
                query =f"update donor set {placeholder} where id =%s"
                values =[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor details Updated Successfully...!")


            else:
                print("Data not Found..!")
        except Exception as e:
            print(e)

donor_instance =BloodDonorManager()
#donor_instance.post(name="Anu",blood_group="A+",phone ="8976543456",city="Alappuzha",last_donation=datetime.datetime.today())
#donor_instance.post(name= "Surya",blood_group="A+",phone="8989768979",city="Eranakulam",last_donation=datetime.datetime.today())
#donor_instance.post(name="Arun", blood_group="B+", phone="9876543210", city="Kozhikode", last_donation=datetime.datetime.today())
#donor_instance.post(name="Meera", blood_group="O+", phone="8765432109", city="Thrissur", last_donation=datetime.datetime.today())
#donor_instance.post(name="Rahul", blood_group="AB+", phone="9654321087", city="Kottayam", last_donation=datetime.datetime.today())
#donor_instance.post(name="Anjali", blood_group="A-", phone="9543210876", city="Kannur", last_donation=datetime.datetime.today())
#donor_instance.post(name="Vishnu", blood_group="O-", phone="9432108765", city="Malappuram", last_donation=datetime.datetime.today())
#donor_instance.post(name="Neha", blood_group="B-", phone="9321087654", city="Alappuzha", last_donation=datetime.datetime.today())
donor_instance.get()
print("_____Details of Retrieved Donor_____")
donor_instance.retrieve(id=4)
print("____After deleting____")
donor_instance.delete(id=1)
print("____After Updation____")
donor_instance.put(2, city="Kochi")
donor_instance.get()