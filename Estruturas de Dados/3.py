# Construa um script que leia uma string e a imprima de forma reversa

string = input("Digite um texto: ");
inverse = ' '.join(inverse[::-1] for inverse in string.split());
print(inverse);