'''from django.db import models
import datetime
import os

def getFileName(request,filename):
	now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
	new_filename="%s%s"%(now_time,filename)
	return os.path.join("uploads/".new_filename)


class property_type(models.Model) :
  id=models.AutoField(primary_key=True)
  description =models.TextField(max_length=500,null=False,blank=True)


def __str__(self):
	return self.description
  

class  Property(models.Model):
  #id=models.IntegerField(null=False,blank=False,primary_key=True)
  address=models.CharField(max_length=150,null=False,blank=False)
 # address_line2=models.CharField(max_length=150)
  city =models.CharField(max_length=100, null=False,blank=False)
  country=models.CharField(max_length=100)
  property_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  property_type_id =models.ForeignKey(property_type,on_delete=models.CASCADE)
  property_size=models.FloatField(null=False,blank=False)    
  description =models.TextField(max_length=500,null=False,blank=True)


def __str__(self):
	return self.address




class listing_type(models.Model): 
 # id=models.IntegerField(null=False,blank=False,primary_key=True)
  description =models.TextField(max_length=500,null=False,blank=True)


class feature(models.Model) :
#  id=models.IntegerField(null=False,blank=False,primary_key=True)
  feature_name =models.CharField(max_length=150,null=False,blank=False)


class property_feature(models.Model) :
  property_id =models.ForeignKey(property,on_delete=models.CASCADE)
  feature_id =models.ForeignKey(feature,on_delete=models.CASCADE)


class listing(models.Model):
  #id =models.IntegerField(null=False,blank=False,primary_key=True) 
  property_id =models.ForeignKey(property,on_delete=models.CASCADE)
 # listing_status_id =models.IntegerField(null=False,blank=False)
  listing_type_id =models.ForeignKey(listing_type,on_delete=models.CASCADE)
  price =models.IntegerField(null=False,blank=False) 
  created_date =models.DateTimeField(auto_now_add=True)


class employee (models.Model):
 # id =models.IntegerField(null=False,blank=False,primary_key=True) 
  first_name  =models.CharField(max_length=100, null=False,blank=False)
  last_name  =models.CharField(max_length=100, null=False,blank=False)
  start_date =models.DateTimeField(auto_now_add=True)
  end_date =models.DateTimeField(auto_now_add=True)
  email_id=models.CharField(max_length=100, null=False,blank=False)
  phone_number=models.IntegerField(null=False,blank=False)

class role_type(models.Model):
  #id =models.IntegerField(null=False,blank=False,primary_key=True)
  description  =models.CharField(max_length=100, null=False,blank=False)
  

class property_employee(models.Model): 
  property_id =models.ForeignKey(property,on_delete=models.CASCADE)
  employee_id =models.ForeignKey(employee,on_delete=models.CASCADE)
  role_type_id =models.ForeignKey(role_type,on_delete=models.CASCADE)
  start_date =models.DateTimeField(auto_now_add=True)
  end_date =models.DateTimeField(auto_now_add=True)



class inspection(models.Model): 
 # id =models.IntegerField(null=False,blank=False,primary_key=True)
  property_id =models.ForeignKey(property,on_delete=models.CASCADE)
  inspection_datetime =models.DateTimeField(auto_now_add=True)
  responsible_employee_id =models.ForeignKey(employee,on_delete=models.CASCADE)


class client(models.Model) :
 # id =models.IntegerField(null=False,blank=False,primary_key=True)
  first_name  =models.CharField(max_length=100, null=False,blank=False)
  last_name  =models.CharField(max_length=100, null=False,blank=False)
  email_address  =models.CharField(max_length=100, null=False,blank=False)
  phone_number  =models.CharField(max_length=100, null=False,blank=False)
  client_image =models.ImageField(upload_to=getFileName,null=True,blank=True)
  aadhar_number=models.IntegerField(null=False,blank=False)

class client_property_interest(models.Model):
  client_id =models.ForeignKey(client,on_delete=models.CASCADE)
  property_id =models.ForeignKey(property,on_delete=models.CASCADE)


class client_inspection (models.Model):
  client_id =models.ForeignKey(client,on_delete=models.CASCADE)
  inspection_id  =models.ForeignKey(inspection,on_delete=models.CASCADE)


class offerStatus(models.Model):
  #id=models.IntegerField(null=False,blank=False)
  description  =models.CharField(max_length=100, null=False,blank=False)

  
class offer(models.Model):
  #id =models.IntegerField(null=False,blank=False,primary_key=True)
  client_id =models.ForeignKey(client,on_delete=models.CASCADE)
  property_id =models.ForeignKey(property,on_delete=models.CASCADE)
  offer_status_id =models.ForeignKey(offerStatus,on_delete=models.CASCADE)
  offer_amount =models.IntegerField(null=False,blank=False)

  

class contract_status(models.Model):
 # id =models.IntegerField(null=False,blank=False,primary_key=True)
  description =models.IntegerField(null=False,blank=False)


class contract(models.Model):
 # id=models.IntegerField(null=False,blank=False,primary_key=True)
  property_id =models.ForeignKey(property,on_delete=models.CASCADE)
  listing_type_id =models.ForeignKey(listing_type,on_delete=models.CASCADE)
  contract_document =models.ImageField(upload_to=getFileName,null=True,blank=True)
  responsible_employee_id =models.ForeignKey(employee,on_delete=models.CASCADE)
  client_id =models.ForeignKey(client,on_delete=models.CASCADE)
  contract_status_id =models.ForeignKey(contract_status,on_delete=models.CASCADE)
  signed_date =models.DateTimeField(auto_now_add=True)
  start_date =models.DateTimeField(auto_now_add=True)
  end_date =models.DateTimeField(auto_now_add=True)

'''
from django.db import models
from django.contrib.auth.models import User
import datetime
import os


def getFileName(instance, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join("uploads/", new_filename)

class PropertyType(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=150,null=False,blank=False)
    description = models.TextField(max_length=500, null=False, blank=True)
    #locality = models.CharField(max_length=100, null=False, blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    image=models.ImageField(upload_to=getFileName,null=False,blank=True)

    def __str__(self):
        return self.description

class Property(models.Model):
    seller=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    address = models.CharField(max_length=150, null=False, blank=False)
    town = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    region = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    Quantity= models.IntegerField(default=0,null=False,blank=False)
    property_size = models.FloatField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    image=models.ImageField(upload_to=getFileName,null=False,blank=True)
    trending=models.BooleanField(default=False,help_text="0-show,1-hidden")
    
    def __str__(self):
        var=self.address +" "+ self.town
        return var

class ListingType(models.Model):
    description = models.TextField(max_length=500, null=False, blank=True)

    def __str__(self):
        return self.description

class Feature(models.Model):
    feature_name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.feature_name

class PropertyFeature(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)

class Listing(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    listing_type_id = models.ForeignKey(ListingType, on_delete=models.CASCADE)
    price = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.price

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    Age = models.IntegerField(null=True, blank=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False)
    email_id = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
   # Name= self.first_name + " " + self.last_name
      return self.email_id

class RoleType(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.description

class PropertyEmployee(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_type_id = models.ForeignKey(RoleType, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)

class Inspection(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    inspection_datetime = models.DateTimeField(auto_now_add=False)
    responsible_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Client(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email_address = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    client_image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    aadhar_number = models.CharField(max_length=100,null=False, blank=False)
    def __str__(self):
      return self.first_name

class ClientPropertyInterest(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)

class ClientInspection(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    inspection_id = models.ForeignKey(Inspection, on_delete=models.CASCADE)

class OfferStatus(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
      return self.description

class Offer(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    offer_status_id = models.ForeignKey(OfferStatus, on_delete=models.CASCADE)
    offer_amount = models.IntegerField(null=False, blank=False)

    def __str__(self):
      return self.offer_amount

class ContractStatus(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
      return self.description


class Contract(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    listing_type_id = models.ForeignKey(ListingType, on_delete=models.CASCADE)
    contract_document = models.ImageField(upload_to=getFileName, null=True, blank=True)
    responsible_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    contract_status_id = models.ForeignKey(ContractStatus, on_delete=models.CASCADE)
    signed_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
      return self.signed_date

class Cart(models.Model):
    user_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE)
    property_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

