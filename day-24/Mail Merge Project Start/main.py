PLACEHOLDER = "[name]"
# letter
with open("Input/Letters/starting_letter.txt") as f_letter:
    letter = f_letter.read()
#print(letter)

# lista com os nomes
# names = []
with open("Input/Names/invited_names.txt") as f_names:
    names = f_names.readlines()
print(names)

for name in names:
    new_name = name.replace("\n", "")
    # texto da carta
    n_letter = letter.replace(PLACEHOLDER, new_name)
    # print(n_letter)

    # nome do arquivo
    name = name.replace(" ", "_")
    name_file = f"letter_for_{name}.txt"

    # caminho do arquivo
    path_with_file = f"Output/ReadyToSend/{name_file}"

    # print(name_file)
    with open(path_with_file, "w", encoding="utf-8") as f:
        f.write(n_letter)