class Factory:

	def engine(self):
		return "Двигатель создан"

	def bridge(self):
		return "Двигатель создан"

class Toyota(Factory):

	def wheels(self):
		return"Колёса готовы"

	def windows(self):
		return "Стёкла готовы"
a = []
y = Toyota()
q = y.wheels()
w = y.windows()
f = Factory()
r = f.engine()
t = f.bridge()
a.append((q, w, r, t))

print(a)
