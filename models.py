from django.db import models

# Create your models here.
class Customer(models.Model):
	name=models.CharField(max_length=255)


class Product(models.Model):
	name=models.CharField(max_length=255)
	customer=models.ManyToManyField(Customer,related_name='Product')


class Office(models.Model):
	office_name=models.CharField(max_length=255)
	def __str__(self):
		return"%s"%(self.office_name)




class Employee(models.Model):
	name=models.CharField(max_length=255)
	mobile=models.CharField(max_length=10)
	department=models.CharField(max_length=255)
	salary=models.IntegerField()
	email=models.EmailField()
	office_name=models.ForeignKey(Office,blank=True,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return "%s"%(self.name)

	
class Movie(models.Model):
		movie_name=models.CharField(max_length=255)
		genre=models.CharField(max_length=255)
		def __str__(self):
			return "%s"%(self.movie_name)

class Song(models.Model):
		song_name=models.CharField(max_length=255)
		movies=models.ForeignKey(Movie,blank=True,null=True,on_delete=models.CASCADE)
		def __str__(self):
			return "%s"%(self.song_name)