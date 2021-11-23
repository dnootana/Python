#!/usr/bin/env python3.8

def infinite_dict_to_tuple(i_dict):
	"""
		given infinite dictionary convert to dictionary with key tuples

	"""
	list_out = []
	for key in dict_a.keys():
		s_dict = {"key":None, "value":None}
		sub_list = [key]
		new_dict = dict_a[key]
		if type(new_dict) is not dict:
			s_dict["value"] = new_dict
		else:
			while 1:
				k = next(iter(new_dict))
				sub_list.append(k)
				new_dict = new_dict[k]
				if type(new_dict) is not dict:
					s_dict["value"] = new_dict
					break
		s_dict["key"] = tuple(sub_list)
		list_out.append(s_dict)
	return list_out

dict_a = {'a':{1:'x'},'b':{'e':{'r':60}}}
A = [{"key":('a',1),"value":'x'},{"key":('b','e','r'),"value":60}]
out_list = infinite_dict_to_tuple(dict_a)
print("output : ",out_list)
print("expected : ",A)