def format_name(f_name, l_name):
    """
    * Takes the first and last name and format it and retturn the title case version of the name.
    """
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
print(format_name(f_name, l_name))