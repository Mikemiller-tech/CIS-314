def generate_heart():
    heart = """
      *****     *****
    *******   *******
   ********* *********
   *******************
    *****************
      *************
        *********
          *****
           ***
            *
    """
    print("\033[31m" + heart + "\033[0m")  # Red heart


def generate_cry_face():
    cry_face = """
      .-\"\"\"\"\"\"\"-.
    .'          '.
   /   (T_T)    \\
  :              :
  |   ----      |
  :   .      .  :
   \\ '------' /
    '.      .'
      '-...-'
    """
    print("\033[34m" + cry_face + "\033[0m")  # Blue crying face


# Ask the user
response = input("Will you be my Valentine? (yes/no): ").strip().lower()

if response == "yes":
    print("Yay! Here's a heart for you:")
    generate_heart()
else:
    print("Oh no! Here's a crying face:")
    generate_cry_face()
