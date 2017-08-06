#service2_init.py
# -*- coding: utf-8 -*- 

class Service2_init():
	secret = "자몽이는 고양이가 아니다."
	def __init__(self, name):
		self.name = name
	def sum(self, a, b):
		result = a + b
		print("%s님, %s + %s = %s" %(self.name, a, b, result))

purification = Service2_init("허정화")
purification.sum(23, 1)