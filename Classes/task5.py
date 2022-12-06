
class Patient():

	def __init__(self, name, age, complaint):
		self.name = name
		self.age = age
		self.complaint = complaint

	def __str__(self):
		return f'name = {self.name}, age = {self.age}, complaint = {self.complaint}'



class Doctor():

	def __init__(self, name, speciality):
		self.name = name
		self.speciality = speciality
		self.time_appointment = {'8:00':'Null','8:30':'Null','9:00':'Null','9:30':'Null',
		'10:00':'Null','10:30':'Null','11:00':'Null','11:30':'Null','12:00':'Null','12:30':'Null',
		'14:00':'Null','14:30':'Null','15:00':'Null','15:30':'Null','16:00':'Null','16:30':'Null'}

	def __str__(self):
		return f'name = {self.name}, speciality = {self.speciality}, {self.time_appointment} '

	def add_patient(self, patient, time_appointment):
		self.time_appointment[time_appointment] = patient



def working_doctor(list_doctors):
	count = 0 
	for x in list_doctors:
		print(count)
		print(x.name)
		print(x.time_appointment)
		count +=1




list_doctors = []
list_patients = []

while True:

	print('Какое действие выполнить? Выберите номер!')
	print('1.Добавить доктора')
	print('2.Добавить пациента')
	print('3. Вывести список работающих докторов')
	print('0. Выход из программы')
	action = int(input())


	

	if action == 1:
		name = input('Введите имя доктора:\n')
		speciality = input('Введите специальность доктора:\n')
		list_doctors.append(Doctor(name, speciality))

	if action == 2:
		name = input('Введите имя пациента:\n')
		age = input('Введите возраст пациента:\n')
		complaint = input('Введите жалобу на здоровье:\n')
		list_patients.append(Patient(name,age,complaint))
		
		working_doctor(list_doctors)
		doctor = int(input('К кааому доктору направить (номер):\n'))
		time = input('Время приема:\n')
		list_doctors[doctor].add_patient(list_patients[-1].name, time)



	if action == 3:
		working_doctor(list_doctors)

	if action == 0 :
		break