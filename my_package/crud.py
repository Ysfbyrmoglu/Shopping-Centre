    from fastapi import Body
from leanapi.path import controller
from leanapi.server import router
from model import Employees,Customers,Products,Sellers,EmployeeCreate,CustomerCreate,ProductCreate,SellerCreate

@controller("Employees",router)
class Employee:

    @router.get("/employee/get/{employee_id}")
    async def get_employee (employee_id:int) ->dict:
        if Employees[employee_id]==employee_id:
            return Employees[employee_id]
        else:
            print('you have not this employee')
    @router.put("/employee/put/{employee_id}")
    async def update_employee(self,employee_id:int=Body(...,enbed=True)):

        Employees["employee_id"]=employee_id

        return Employees

    @router.post("/employee/create")
    async def create_employee(self,EmployeeCreate ) :
        return employee

    @router.delete("/employee/delete/{employee_id}")
    async def delete_employe(self,employee_id:int):
        if employee_id in Employees:
            Employees.pop[employee_id]
            return Employees
        else:
            return {'data':'employee is not found'}

@controller("Customers",router)
class Customer:
    @router.get("/customer/get/{customer_id}")
    async def get_customer(self,customer_id:int):
        if Customers[customer_id]==customer_id:
            return Customers
        else:
            print("You have not this Customer")

    @router.put("/customer/put/{customer_id}")
    async def update_customer(self,customer_id:int=Body(...,enbed=True,)):
        Customers[customer_id]=customer_id
        return Customers

    @router.post("/customer/create")
    async def create_customer(self,CustomerCreate):
        return customer

    @router.delete("/customer/delete/{customer_id}")
    async def delete_customer(self,customer_id):
        if customer_id in Customers:
            Customers.pop[customer_id]
            return Customers
        else:
            print("you already have not this customer")

@controller("Products",router)
class product:

    @router.get("/product/get/{product_id}")
    async def get_product(self,product_id:int):
        if Products[product_id]==product_id:
            return product
        else:
            print("you have not this product")


    @router.put("/product/put/{product_id}")
    async def update_product(self,product_id:int=Body(...,enbed=True)):
        product[product_id]=product_id
        return product
    @router.post("/product/create")
    async def creat_product(self,ProductCreate):
        return product
    @router.delete("/product/delete/{product_id}")
    async def delete_product(self,productid):
        if productid in Products:
            Products.pop[productid]
        else:
            print("you already dont have this product")


@controller("Sellers",router)
class Seller:
   
    @router.get("/Seller/get/{company_id}")
    async def get_seller(self,company_id:int):
    if Seller[company_id]==company_id:
        return Seller
    else:
        print("you have not this seller")


    @router.put("/put/seller")
    async def update_seller(self,company_id:int=Body(...,enbed=True)):
        Seller["company_id"]=company_id
        return Seller
   

    @router.post ("/Seller/create")
    async def create_seller(self,SellerCreate):
        return seller 


    @router.delete("/seller/delete")
    async def delete_seller(self,company_id:int)
    if company_id in seller:
       seller.pop[company_id]

    else: 
        print("you already have not this seller")



