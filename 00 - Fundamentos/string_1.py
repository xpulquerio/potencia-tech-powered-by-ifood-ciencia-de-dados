#Maiúsculo, minúsculo e título
curso = "pYthon"
print(curso.upper())
print(curso.lower())
print(curso.title())

#Eliminar espaços em branco
curso = "    pYthon "
print(curso.strip()) #tira os espaços left-right
print(curso.lstrip()) #left-strip
print(curso.rstrip()) #right-strip

#Junções e Centralização
curso = "Python"
print(curso.center(9, "#"))
print(".".join(curso))

