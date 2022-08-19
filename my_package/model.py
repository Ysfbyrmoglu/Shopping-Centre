from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from postgresql import relationship

from Database import Base



class Employees(Base):
    __tablename__ = 'employee'
employee_id= Column(Integer,primary_key=True)
employee_name=Column(String)
employee_surname=Column(String)
employee_age=Column(Integer)
employee_email=Column(String,unique=True)
employee_phone=Column(Integer,unique=True)
wage=Column(Float)

class EmployeeCreate(Employees):
    pass

class Customers(Base):
     __tablename__="customer"
customer_id=Column(Integer,primary_key=True)
TCNumberOrPassportNumber=Column(Integer,unique=True)
customer_phone=Column(Integer,unique=True)
customer_name=Column(String)
customer_surname=Column(String)
customer_type=Column(String)
balance=Column(Float)
explamation=Column(String)
address=Column(String)

class CustomerCreate(Customers):
    pass



class Products(Base):
    __tablename__= "product"
product_id:Column(Integer,primary_key=True)
product_name=Column(String)
product_tpye=Column(String)
unit=Column(String)
price=Column(Float)

class ProductCreate(Products):
    pass



class Sellers(Base):
    __tablename__="seller"
company_id=Column(Integer,primary_key=True)
company_name=Column(String)
company_phone=Column(Integer)
company_address=Column(String)
receivable=Column(Float)
company_email=Column(String)

class SellerCreate(Sellers):
    pass

