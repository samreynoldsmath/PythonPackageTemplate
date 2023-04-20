from .. import src2

def hello_from_other_subpackage():
	print('calling a function from src2.mod_x')
	src2.mod_x.hello()
	print('goodbye from src1.mod_c')