
# Введення (отримання даних)
name_client = input("Введіть ваше ім'я: ")

# Перетворення (обробка даних)
greeting_client = f"Привіт in Title, {name_client.title()}!"
greeting_in_lowercase = f"Привіт in lowecase, {name_client.lower()}!"
greeting_in_uppercase = f"Привіт in uppercase {name_client.upper()}!"
all_greetings = greeting_client + "\n" + greeting_in_lowercase + "\n\t" + greeting_in_uppercase

# Виведення (виведення даних)
print(greeting_client)
print(greeting_in_lowercase)
print(greeting_in_uppercase)
print(all_greetings)


