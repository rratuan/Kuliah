#I.F inputkan jarak tempuh semut dalam cm
#F.S outputkan km,m dan cm jarak semut

totaljarak = int(input("Jarak tempuh semut : "))

km = totaljarak // 100000
sisakm = totaljarak % 100000

m = sisakm // 100
cm =sisakm % 100

print("Jarak Tempuh Semut Sejauh :", km , "Kilometer |", m , "Meter |", cm , "Centimeter |") 