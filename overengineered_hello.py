import asyncio

async def hex_to_string(hex_to_string_boolean):
	if hex_to_string_boolean:
		hex_values = ["48", "65", "6c", "6c", "6f", "2c", "20", "57", "6f", "72", "6c", "64", "21"]
		global string_text
		string_text = []
		for i in hex_values:
			string_text.append(bytearray.fromhex(i).decode())
async def createClass(createClass_boolean):
	if createClass_boolean == True:
		global Hello_World_Class
		class Hello_World_Class:
			def __init__(self, tuple_string, print_boolean):
				self.tuple_string = tuple_string
				self.print_boolean = print_boolean
				self.output = []
			def print_tuple_string(self, print_tuple_boolean):
				if self.print_boolean == True:
					if print_tuple_boolean:
						for i in self.tuple_string:
							self.output.append(i)
async def initialize(initialize_boolean, return_boolean, hex_boolean):
	if hex_boolean == True:
		await hex_to_string(True)
	if initialize_boolean:
		await createClass(True)
		def H_function(H_boolean):
			if H_boolean == True:
				global H
				H = string_text[0]
		def e_function(e_boolean):
			if e_boolean == True:
				global e
				e = string_text[1]
		def l_function(l_boolean):
			if l_boolean == True:
				global l
				l = string_text[2]
		def second_l_function(second_l_boolean):
			if second_l_boolean == True:
				global second_l
				second_l = string_text[3]
		def o_function(o_boolean):
			if o_boolean == True:
				global o
				o = string_text[4]
		def comma_function(comma_boolean):
			if comma_boolean == True:
				global comma
				comma = string_text[5]
		def space_function(space_boolean):
			if space_boolean == True:
				global space
				space = string_text[6]
		def W_function(W_boolean):
			if W_boolean == True:
				global W
				W = string_text[7]
		def second_o_function(second_o_boolean):
			if second_o_boolean == True:
				global second_o
				second_o = string_text[8]
		def r_function(r_boolean):
			if r_boolean == True:
				global r
				r = string_text[9]
		def third_l_function(third_l_boolean):
			if third_l_boolean == True:
				global third_l
				third_l = string_text[10]
		def d_function(d_boolean):
			if d_boolean == True:
				global d
				d = string_text[11]
		def exclamation_mark_function(exclamation_mark_boolean):
			if exclamation_mark_boolean == True:
				global exclamation_mark
				exclamation_mark = string_text[12]
		H_function(True)
		e_function(True)
		l_function(True)
		second_l_function(True)
		o_function(True)
		comma_function(True)
		space_function(True)
		W_function(True)
		second_o_function(True)
		r_function(True)
		third_l_function(True)
		d_function(True)
		exclamation_mark_function(True)
		list_string = []
		list_string.append(H)
		list_string.append(e)
		list_string.append(l)
		list_string.append(second_l)
		list_string.append(o)
		list_string.append(comma)
		list_string.append(space)
		list_string.append(W)
		list_string.append(second_o)
		list_string.append(r)
		list_string.append(third_l)
		list_string.append(d)
		list_string.append(exclamation_mark)
		boolean = True
		hello_world = Hello_World_Class(tuple(list_string), boolean)
		hello_world.print_tuple_string(True)
		if return_boolean == True:
			return hello_world.output
def print_string(empty_boolean, for_boolean, link_to_initialize_boolean, end_to_empty_variable_boolean, print_string_boolean, hex_boolean):
	if empty_boolean == True:
		global empty
		empty=''
		global stop
	if for_boolean == True:
		if link_to_initialize_boolean == True:
			for output in asyncio.run(initialize(True, True, hex_boolean)):
				if end_to_empty_variable_boolean == True:
					if print_string_boolean:
						print(output, end=empty)
print_string(True, True, True, True, True, True)
