#!/usr/bin/python3

#print(1 + 1)
#print(__name__)
#if __name__ == '__main__':
#    print("do something")

#section 2 ----------------------

#x = 2 + 3 \
#        + 5 \
#        + 10
#
#print(x)

#section 3 TYPE DATE----------------------
#num = 0
#text = ""
#
#num, text = 12, "Testing"
#print(num, text)
#
#print(type(num))
#print(type(text))
#
#my_list = ["texto", "texto2", "texto3"]
#t1 = ""
#t2 = ""
#t3 = ""
#
#t1, t2, t3 = my_list
#
#print(my_list)
#print(t1)
#print(t2)
#print(t3)
#
#print(type(my_list))
#
#my_tuple = ("tupla1", "tupla2")
#print(my_tuple)
#print(type(my_tuple))
#
#my_dictionary = {"john": 1, "buff": 2, "burp": 3}
#print(my_dictionary)
#print(type(my_dictionary))
#
#my_boolean = True
#print(my_boolean)
#print(type(my_boolean))
#
#my_range = range(6)
#print(my_range)
#print(type(my_range))
#
#my_byte = b"my byte"
#print(my_byte)
#print(type(my_byte))

#section 4 NUMBERS----------------------
#my_num = 12
#my_float = 23
#my_complex_num = 12j
#my_octal_num =  0o12
#my_hexadecimal_num = 0x10
#
#print(type(my_num))
#print(type(my_float))
#print(type(my_complex_num))
#print(type(my_octal_num))
#print(type(my_hexadecimal_num))
#
#
#print(my_num)
#print(my_float)
#print(my_complex_num)
#print(my_octal_num)
#print(my_hexadecimal_num)
#
#my_num = bin(10)
#print(type(my_num))
#print(my_num)
#
#my_num = hex(10)
#print(type(my_num))
#print(my_num)
#
#my_num = oct(10)
#
#print(type(my_num))
#print(my_num)
#print(type(my_num))
#
#print(abs(2))
#print(abs(-2))
#
#print(round(9.9))
#print(round(9.3))
#print(round(9.5))

#section 5  STRINGS ----------------------

#my_str = "I am string "
#my_str_2 = "I am string too"
#simple_str = "a" 
#my_character = "characteres \\ \" \' \\0x2"
#mul_str = 20 * "a"
#
#print(my_character )
#print(my_str)
#print(my_str_2 )
#print(simple_str)
#print(mul_str )
#
#print(my_str.startswith("I"))
#print(my_str.startswith("F"))
#print(my_str_2.index("too"))
#print("am" in my_str)
#print("saldfk" in my_str)
#
#my_custom_str = "      Programing with Python!!!     "
#print(my_custom_str)
#print(my_custom_str.strip()) #strip (quitar) {quita las lineas en blanco}
#print(my_custom_str.replace("!", "\\"))
#print(my_custom_str.replace("!", "\\").strip())
#
#
#my_cstm_str = "welcome back ethical hacking"
#my_c_str = "welcome,back,ethical,hacking"
#print(my_cstm_str.split())
#print(my_c_str.split(","))
#print(my_c_str.split())
#
#
#my_string = "Pentesting active directory"
#print(my_string.encode())
#print(my_string.encode("utf-8"))
#print(my_string.rjust(50))
#print(my_string.rjust(50, '='))
#print(my_string.ljust(50))
#print(my_string.ljust(50, 'x'))
#
#my_name = "My name is hax01"
#
#print("My name is lengt {}".format(len(my_name)))
#print("{} {} {}".format(len(my_name), 12, 23))
#print("{2} {1} {0}".format(len(my_name), 60, 50))
#
#print("my_name is {lenght:.2f} characters long!".format(lenght=len(my_name)))
#print("my_name is {lenght:.3f} characters long!".format(lenght=len(my_name)))
#print("my_name is {lenght:.4f} characters long!".format(lenght=len(my_name)))
#
#print("my number is {lenght:b}".format(lenght=len(my_name)))
#print("my number is {lenght:x}".format(lenght=len(my_name)))
#print("my number is {lenght:o}".format(lenght=len(my_name)))
#print("my number is {lenght:f}".format(lenght=len(my_name)))
#
#lenght = len(my_name)
#print(f'my_name is {lenght}')
#
#print("my favorite number is %d " % 12)
#print("my favorite number is %f" % 34.234)
#print("my favorite number is 0x %x" % len(my_name))

#section 6  Booleans operators ----------------------
#valid = True
#not_valid = False
#
#print(valid)
#print(not_valid)
#
#print(valid == True)
#print(not_valid == True)
#
#print(valid != True)
#print(not_valid != True)
#
#print(not valid)
#print(not not_valid)
#
#print("---------")
#print((5 > 3 ) == True)
#print((5 >= 8) == True)
#print((9 <= 1 )== True)
#print((90 == 100) == True)
#print((1 != 0) == True)
#print("---------")
#
#print(3 == 3)
#print(0 > 9)
#print(3 < 1)
#print(9 <= 11)
#print(5 >= 5)
#print(0 != 0 )
#
#print("---------")
#print(3 > 1 and 5 > 2)
#print(8 > 10 or 9 == 9)
#print("---------")
#
#print(bool(1))
#print(bool(0))
#print(bool(1) == False)
#print(bool(0) == False)
#print("---------")
#
#print(9 + 9)
#print(0 - 12)
#print(40 * 2)
#print(80 / 2)
#print(80 // 2)
#print(20 ** 2)
#print(20 % 5)
#print("---------")
#
#x = 20
#print(x)
#x = x +1
#print(x)
#x +=1
#print(x)
#x -=1
#print(x)
#x *=2
#print(x)
#x %=2
#print(x)
#x /=2
#print(x)
#x = 20
#x **=3
#print(x)
#x //=9
#print(x)
#print("---------")
#
#print(bin(10))
#print(bin(10)[2:])
#print(bin(10)[2:].rjust(4, 'X'))
#
#x = 4
#y = 3
#print(bin(x & y))
#print(bin(x & y)[2:])
#
#print(bin(x)[2:])
#print(bin(x >> 1)[2:])
#print(bin(x << 1)[2:])
#section 7 Tuples----------------------
#tuple_items = ("item1", "item2", "item3")
#print(tuple_items)
#print(type(tuple_items))
#
#tuple_number = (10, 11, 12)
#print(tuple_number)
#print(type(tuple_number))
#
#tuple_repeat = ("repeat",) * 4 
#print(tuple_repeat)
#print(type(tuple_repeat))
#
#tuple_mixed = (1, "A", (1, "A"))
#print(tuple_mixed)
#print(type(tuple_mixed))
#
#tuple_combined = tuple_items + tuple_number
#print(tuple_combined)
#
#item1, item2, item3 = tuple_items
#print(item1)
#print(item2)
#print(item3)
#
#print("item1" in tuple_items)
#print("item2" in tuple_items)
#print("item4" in tuple_items)
#
#print(tuple_items.index("item1"))
#print(tuple_items.index("item2"))
#
#print(tuple_items[0])
#print(tuple_items[1])
#print(tuple_items[2])
#
#print(tuple_items[-1])
#print(tuple_items[0:-2])
#print(tuple_items[:-2])
#print(tuple_items[-3:-1])
#
#string = "I'm string good bye!"
#print(string[-1])
#print(string[0:-4])
#section 2 List ----------------------

list_1 = ["A", "B", "C", "D"]
print(list_1)
print(type(list_1))

list_2 = ["A", "B", [], list(), ["A", "B", "C"]]
print(list_2)
print(type(list_2))

print(list_1[0])
print(list_1[-1])

print(list_2[-1][-1])

list_1[0] = "test"
print(list_1)
del list_1[0]
print(list_1)

list_1.insert(0, "new_test")
print(list_1)

del list_1[0]
print(list_1)

list_1 = ["hax"] + list_1
print(list_1)

list_1 = list_1 + ["new_hax"]
print(list_1)

list_1.append("append")
print(list_1)

print(min(list_1))
print(max(list_1))

print(list_1.index("hax"))
print(list_1[list_1.index("hax")])

list_1.reverse()
print(list_1)
list_1 = list_1[::-1]
print(list_1)

list_1.append("hax")
print(list_1)
print(list_1.count("hax"))

list_1.pop()
print(list_1)

list_3 = ["H", "I", "J"]

list_1.extend(list_3)
print(list_1)


list_1.clear()
print(list_1)

list_4 = [12, 2, 5, 0, 9, 12, 234, 1]
print(list_4)

list_4.sort()
print(list_4)

list_4.sort(reverse=True)
print(list_4)

list_5 = list_4

print(list_4)
print(list_5)

list_5[2] = "X"
print(list_5)
print(list_4)

list_6 = list_5.copy()

list_6[2] = "remaster"
print(list_5)
print(list_6)

list_7 = ["1", "2", "3", "4"]
print(list_7)

list_8 = list(map(float, list_7))
print(list_8)







