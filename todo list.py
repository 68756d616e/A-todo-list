# A simple todo list

print("Welcome to your todo list")

list = ['cake', 'bicsuits']

while True:
    # Ask if they want to action anyting
    todo = input("Would you like to add or view your todo, yes or no?: ")
    
    # Ask if they would like to add or edit
    if todo == 'yes':
        question = input("Would you like to 'view', 'remove', or 'add'from your todo list? ")

# change the code below to match the updated question
        if todo == "yes":
          if question == "view":
              print(f"Here is your list of todos: {list}")
              question2 = input("Would you like to 'add' or 'remove' from your todo? ")
              if question2 == "add":
                    item = input("Enter an item you would like to add: ")
                    list.append(item)
              elif question2 == "remove":
                print("First remove works")
              elif question2 != "add" or question2 != "remove":
                print("First break")
              break
  
          elif question == "remove":
              print("remove works")

          elif question == "add":
              print("Add works")

    elif todo == 'no':
        print("You can update later")
        break

    else:
        print("Incorrect : Please input yes or no")