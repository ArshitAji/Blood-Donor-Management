import mysql.connector
import datetime
#from mysql import connector

class BloodDonorManagement:
    def __init__(self):
        self.connection=mysql.connector.connect(     #connector.connect( only need, no need of "mysql"
            host="localhost",
            user="arshi",
            password="arshi",
            database="blood_db"

        )
        print("Connected Successfully")

    def get_object(self,id=None):
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
            self.cursor=self.connection.cursor()
            query="""
                 insert into donor(name,blood_group,phone,city,last_donation)
                 values(%s ,%s ,%s ,%s,%s)
            """
            values=[x for x in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor added successfully")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            for data in record:
                print(data)
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record==None:
                print("record not found")
            else:
                print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            values=(id,)
            if record!=None:
                query="""
                   delete from donor
                   where id=%s
                """
                self.cursor.execute(query,values)
                self.connection.commit()
                print("deleted id from donor table")
            else:
                print("Donor not found")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:#if record is found continue operation
                self.cursor=self.connection.cursor()
                placeholder=""#created empty string
                for k in kwargs.keys():
                    placeholder = placeholder + k +"=%s, "
                    placeholder=placeholder.rstrip(", ")
                    #this is necessary bcoz we don't want a comma imemdiatly before
                    query=f"update donor set {placeholder} where id =%s"
                    values=[v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Donor updated successfully..")
            else:
                print("Donor nor found")
        except Exception as e:
            print(e)

donor_instance=BloodDonorManagement()
# donor_instance.post(name="Albin",blood_group="A-",phone="9854236789",city="Aluva",last_dpnation=datetime.date.today())
# donor_instance.post(name="Sreelal",blood_group="B+",phone="4567892536",city="Rajagiri",last_dpnation=datetime.date.today())
donor_instance.get()
print("-------------------------")
donor_instance.retrieve(id=1)
print("Deleting id =6")
donor_instance.delete(id=6)
donor_instance.get()
print("-----Donor Updated Table------")
donor_instance.put(1,city="Aranmula")
donor_instance.get()
