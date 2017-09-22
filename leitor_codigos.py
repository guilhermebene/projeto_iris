codigo = input()
my_file = open("Códigos Institutos", "r")
for f in range (90):
   line = my_file.readline()
   if  == int(codigo)):
   print(line)         
my_file.close()
