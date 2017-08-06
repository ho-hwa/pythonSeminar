#service2.py
# -*- coding: utf-8 -*- 

class Service2:
	secret = "자몽이는 사실 고양이가 아니다."
	def setname(self, name):
		self.name = name
	def sum(self, a, b):
		result = a + b
		print("%s님, %s + %s = %s" %(self.name, a, b, result))

purification = Service2()
purification.setname("허정화")
purification.sum(23, 1)