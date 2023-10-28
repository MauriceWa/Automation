


print("Hello Mark Bin, here are the options available for you to choose from:\n"
      "1. Business\n"
      "2. Entertainment\n"
      "3. General\n"
      "4. Health\n"
      "5. Science\n"
      "6. Sport\n"
      "7. Technology\n")
while True:
    try:
        category = int(input('Which would you like to choose?\n' 'Input a number please: '))
    except ValueError:
        print("Please input a number")



