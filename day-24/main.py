# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", "a") as file:
#     file.write("\nNew text.")

with open("/Users/55619/Desktop/new_file.txt", "a") as file:
    file.write("\nSomething...")

with open("../../../../Desktop/new_file.txt") as file:
    print(file.read())