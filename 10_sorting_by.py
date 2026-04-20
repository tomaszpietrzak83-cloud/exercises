# As an introduction to sorting lists in Python you'll have to implement two functions.
# In this exercise we represent students as a pair of (mark, full_name), so a tuple of two elements.
def sort_by_mark(my_class):
    return sorted(my_class, key=lambda student: student[0], reverse=True)


def sort_by_name(my_class):
    return sorted(my_class, key=lambda student: student[1])


my_class = [(50, "Alan"), (25, "Shannon"), (75, "Ada")]

print(sort_by_mark(my_class))
print(sort_by_name(my_class))
