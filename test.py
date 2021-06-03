from main import Main

my_object = Main()
x = my_object.get_fields(Main.dirs['Love'])
print(x)
test_list = my_object.ask_to_fill(x)
