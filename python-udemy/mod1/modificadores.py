f = 80  / 6
print(f"\n modificador float: {f:f}")

s = "pedro"
print (f"\n modificador str: {s:s}")

d = 123456789
print (f"\n modificador int: {d:d}")
 
var = "pedro"
print(f"{var:0^10s} \n")

floa = 123
print(f"{floa:0^10f} \n")

flod = 123
print(f"{flod:0>10.2f} \n")

dec = 123
print(f"{dec:0^10d}")

nome = "pedro"
nome = nome.ljust(10, "#")
print(nome)