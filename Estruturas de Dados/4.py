""" Construa um script que leia duas strings: o nome e, em seguida, o sobrenome de uma pessoa.
Imprima esse nome/sobrenome no formato de citação bibliográfica. Ex.: se o nome for João, e
o sobrenome Silva, seu script deverá imprimir “Silva, J.”. """

nome = str(input("Nome: "));
abrev = nome[0];
sobreNome = str(input("Sobremone: "));

print("”" + sobreNome + ", " + abrev+".”");