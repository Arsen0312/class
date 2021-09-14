class Zoo:
	def __init__(self):
		self.animal_1 = "Тигр"
		self.animal_2 = "Бегемот"
		self.animal_3 = "Жираф"

z = Zoo()
z.animal_1 = "Лев"
print(z.animal_1)
a = z.animal_4 = [z.animal_2, z.animal_3]
print(a)
z.animal_3 = "Змея"
print(z.animal_3)