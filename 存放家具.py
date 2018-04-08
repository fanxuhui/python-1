#coding:utf-8


class Home:
	"""docstring for Home"""
	def __init__(self,new_area,new_info,new_address):
		self.area = new_area
		self.info = new_info
		self.address = new_address
		self.left_area = new_area
		self.contain_items=[]

	def __str__(self):
		mesg = "房子的面积是:%d,房子的可用面积:%d,房子的户型是:%s,房子的地址是在:%s"%(self.area,self.left_area,self.info,self.address)
		mesg +=" 当前房子里的物品有:%s"%(str(self.contain_items))
		return mesg

	def add_item(self,item):
	#第一种方法:直接用
		#self.left_area -= item.areas
		#self.contain_items.append(item.name)
	

	#第二种方法:调用方法使用
		self.left_area -=item.get_area()
		self.contain_items.append(item.get_name())



class Bed():
	"""docstring for Bed"""
	def __init__(self,new_name,new_area):
		self.name = new_name
		self.areas = new_area

	def __str__(self):
		return "%s占用的面积是:%d"%(self.name,self.areas)

	def get_area(self):
		return self.areas

	def get_name(self):
		return self.name


myjia = Home(122,"三室一厅","上海市浦东新区世纪大道199号")
print(myjia)


bed1 = Bed("席梦思",4)
print(bed1)
myjia.add_item(bed1)
print(myjia)

bed2 = Bed("三人床",5)
print(bed2)
myjia.add_item(bed2)
print(myjia)
		
		
