my_dict={'b':2,'a':1,'c':3,'d':4}
asc_dict=dict(sorted(my_dict.items()))
des_dict=dict(sorted(my_dict.items(),reverse=True))
print("orginal dictionary:",my_dict)
print("ascending order:",asc_dict)
print("descending order:",des_dict)