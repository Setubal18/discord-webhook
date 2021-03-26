def converteBinarioReal(string):
        if(len(string)==8):
            return float(f'{int(string[:2], 2)}.{int(string[3::], 2)}')
        else:
            raise Exception('I know Python!')  # Don't! If you catch, likely to hide bugs.

    #recebe uma string com oito valores 'zero' ou 'um' sendo os dois primeiros
    #equivalentes à parte inteira e os seis restantes equivalente à parte
    #fracionária de um número binário.
    #A função deverá retornar este número convertido para um número real (float)

print(converteBinarioReal('1100110011'))
# saida na tela: 3.12print(converteBinarioReal('110011001'))
# saida na tela: 3.12print(converteBinarioReal('110011001'))
# saida na tela: 3.12print(converteBinarioReal('110011001'))
# saida na tela: 3.12