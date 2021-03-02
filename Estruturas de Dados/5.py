'''Construa um script que simule a função de “localizar/substituir”. O script deverá ler 3 strings:
uma contendo um texto inicial, a outra contendo a palavra que se deseja substituir, e a outra
contendo a palavra para a qual se deseja substituir. Imprima o texto inicial após a substituição'''

texto = str(input('Entre com seu texto: '));
subs1 = str(input('Qual palavra deseja substituir? '));
subs2 = str(input('Por qual palavar será substituida? '));
texto = texto.replace(subs1, subs2);
print(texto);