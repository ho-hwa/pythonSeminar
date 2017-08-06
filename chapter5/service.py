#service.py
# -*- coding: utf-8 -*- 

class Service:

	secret = "자몽이는 사실 고양이가 아니다."

	def sum(self, a, b):
		result = a + b
		print("%d와 %d를 더한 값은 %s입니다." %(a,b,result))

pey = Service()

print(pey.secret)
print(pey.sum(2,4))