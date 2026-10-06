# from nepafaker_pkg import names

# data = names.load_names()
# print(data[0])

from nepafaker_pkg import names

data = names.load_all_data()
print(list(data.keys()))      # shows which files got loaded
print(data["names_bahun_chhetri"])   # peek at one file's content