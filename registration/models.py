from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
	customer_id = models.CharField(max_length=100,primary_key=True)
	customer_name = models.CharField(max_length=100)
	customer_email = models.CharField(max_length=50)
	customer_phone = models.CharField(max_length=10)
	customer_password = models.CharField(max_length=100)
	def __unicode__(self):
		return self.customer_id
	class Meta:
		db_table = 'customer_tbl'

class Shop(models.Model):
	shop_id = models.CharField(max_length=100,primary_key=True)
	shop_name = models.CharField(max_length=100)
	shop_address = models.CharField(max_length=200)
	shop_area = models.CharField(max_length=100)
	min_discount = models.IntegerField(default=5)
	def __unicode__(self):
		return self.shop_id
	class Meta:
		db_table = 'shop_tbl'

class Shopkeeper(models.Model):
	shopkeeper_id = models.CharField(max_length=100,primary_key=True)
	shopkeeper_name = models.CharField(max_length=100)
	shopkeeper_email_id = models.CharField(max_length=50)
	shopkeeper_phone_number =  models.CharField(max_length=10)
	shopkeeper_password =  models.CharField(max_length=100)
	shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
	def __unicode__(self):
		return self.shopkeeper_id
	class Meta:
		db_table = 'shopkeeper_tbl'

class Category(models.Model):
	category_id = models.CharField(max_length=3,primary_key=True)
	category_name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.map_id
	class Meta:
		db_table = 'category_tbl'

class ShopCategoryMapping(models.Model):
	map_id = models.CharField(max_length=100,primary_key=True)
	shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
	discount_percent = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return self.map_id
	class Meta:
		db_table = 'shop_category_mapping_tbl'