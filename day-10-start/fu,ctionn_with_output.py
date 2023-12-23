#Function with outputs

def format_name(f_name, l_name):
  if f_name == l_name == "" :
    return " You didn't provide valid inputs."
  format_f_name = f_name.title()
  format_l_name = l_name.title()
  return f"Result: {format_f_name} {format_l_name} "

print(format_name(input("what is your first name? "), input("what is your last name?")))

