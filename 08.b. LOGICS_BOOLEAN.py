# Python3 program to illustrate
# working of AND gate
 
def AND (a, b):
 
    if a == 1 and b == 1:
        return True
    else:
        return False
 
# Driver code
if __name__=='__main__':
    print(AND(1, 1))
 
    print(" +-----------------------------------------+")
    print(" |                  AND                    |")
    print(" +----------------------+------------------+")
    print(" | A = False, B = False | A AND B =",AND(False,False)," | ")
    print(" | A = False, B = True  | A AND B =",AND(False,True)," | ")
    print(" | A = True, B = False  | A AND B =",AND(True,False)," | ")
    print(" | A = True, B = True   | A AND B =",AND(True,True),"  |")
    print(" +----------------------+------------------+")

print("\n")
# Python3 program to illustrate
# working of NAND gate

def NAND (a, b):
	if a == 1 and b == 1:
		return False
	else:
		return True

# Driver code
if __name__=='__main__':
	print(NAND(1, 0))
	print(" +-----------------------------------------+")
	print(" |                 NAND                    |")
	print(" +-----------------------------------------+")
	print(" | A = False, B = False | A AND B =",NAND(False,False),"  | ")
	print(" | A = False, B = True  | A AND B =",NAND(False,True),"  | ")
	print(" | A = True, B = False  | A AND B =",NAND(True,False),"  | ")
	print(" | A = True, B = True   | A AND B =",NAND(True,True)," | ")
	print(" +-----------------------------------------+")

print("\n")
# Python3 program to illustrate
# working of OR gate

def OR(a, b):
	if a == 1 or b ==1:
		return True
	else:
		return False

# Driver code
if __name__=='__main__':
	print(OR(0, 0))

	print(" +-----------------------------------------+")
	print(" |                   OR                    |")
	print(" +-----------------------------------------+")
	print(" | A = False, B = False | A OR B =",OR(False,False),"  | ")
	print(" | A = False, B = True  | A OR B =",OR(False,True),"   | ")
	print(" | A = True, B = False  | A OR B =",OR(True,False),"   | ")
	print(" | A = True, B = True   | A OR B =",OR(True,True),"   |")
	print(" +-----------------------------------------+")

print("\n")
# Python3 program to illustrate
# working of NOR gate

def NOR(a, b):
	if(a == 0) and (b == 0):
		return 1
	elif(a == 0) and (b == 1):
		return 0
	elif(a == 1) and (b == 0):
		return 0
	elif(a == 1) and (b == 1):
		return 0

# Driver code
if __name__=='__main__':
	print(NOR(0, 0))

	print(" +-------------------------------------+")
	print(" |                  NOR                |")
	print(" +-------------------------------------+")
	print(" | A = False, B = False | A NOR B =",NOR(False,False)," | ")
	print(" | A = False, B = True  | A NOR B =",NOR(False,True)," | ")
	print(" | A = True, B = False  | A NOR B =",NOR(True,False)," | ")
	print(" | A = True, B = True   | A NOR B =",NOR(True,True)," | ")
	print(" +-------------------------------------+")

print("\n")
# Python3 program to illustrate
# working of Xor gate
 
def XOR (a, b):
    if a != b:
        return 1
    else:
        return 0
 
# Driver code
if __name__=='__main__':
    print(XOR(5, 5))
    print(" +-------------------------------------+")
    print(" |                  XOR                |")
    print(" +-------------------------------------+")
    print(" | A = False, B = False | A XOR B =",XOR(False,False)," | ")
    print(" | A = False, B = True  | A XOR B =",XOR(False,True)," | ")
    print(" | A = True, B = False  | A XOR B =",XOR(True,False)," | ")
    print(" | A = True, B = True   | A XOR B =",XOR(True,True)," |")
    print(" +-------------------------------------+")



print("\n")	
# Python3 program to illustrate
# working of Not gate

def XNOR(a,b):
	if(a == b):
		return 1
	else:
		return 0
# Driver code
if __name__=='__main__':
	print(XNOR(1,1))

	print("+--------------------------------------+")
	print("|                  XNOR                |")
	print("+--------------------------------------+")
	print("| A = False, B = False | A XNOR B =",XNOR(False,False)," | ")
	print("| A = False, B = True  | A XNOR B =",XNOR(False,True)," | ")
	print("| A = True, B = False  | A XNOR B =",XNOR(True,False)," | ")
	print("| A = True, B = True   | A XNOR B =",XNOR(True,True)," | ")
	print("+--------------------------------------+")

print("\n")
# Python3 program to illustrate
# working of Not gate
def NOT(a):
	return not a
# Driver code
if __name__=='__main__':
	print(NOT(0))

	print("+---------------------------+")
	print("|              NOT          |")
	print("+---------------------------+")
	print("| A = False | A NOT =",NOT(False)," | ")
	print("| A = True, | A NOT =",NOT(True),"| ")
	print("+---------------------------+")

