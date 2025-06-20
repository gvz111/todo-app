# from functions import get_todos, write_todos
import functions
import time


now=time.strftime('%b %d, %Y %H:%M:%S')
print(now)

while True:
	user_action = input("Type add, show, edit, complete or exit: ")
	user_action = user_action.strip()

	if user_action.startswith('add'):
		todo = user_action[4:]

		todos=functions.get_todos()

		todos.append(todo+'\n')

		functions.write_todos(todos,'todos.txt')
	
	elif user_action.startswith('show'):

		todos=functions.get_todos()

		# new_todos=[item.strip('\n') for item in todos]

		for index, item in enumerate(todos):
			item=item.strip('\n') #coments for this
			row=f"{index+1}-{item}"
			print(row)

	elif user_action.startswith('edit'):
		try:
			number = int(user_action[5:])
			print(number)
			number = number-1

			todos=functions.get_todos()

			new_todo = input("Enter new todo: ")
			todos[number] = new_todo+'\n'

			# with open('todos.txt', 'w') as file:
			# 	file.writelines(todos)
			functions.write_todos(todos)
		except ValueError:
			print("Invalid command.")
			continue

	elif user_action.startswith('complete'):
		try:
			number = int(user_action[9:])
			
			todos=functions.get_todos()
			index=number-1
			todo_to_remove=todos[index].strip('/n')
			todos.pop(index)

			# with open('todos.txt', 'w') as file:
			# 	file.writelines(todos)
			functions.write_todos(todos)

			message=f"Todo: {todo_to_remove}was removed from the list."
			print(message)
		except IndexError:
			print('There is no item with such number.')
			continue
	
	elif user_action.startswith('exit'):
		break
	else:
		print("Invalid command!")

print(" Bye! ")