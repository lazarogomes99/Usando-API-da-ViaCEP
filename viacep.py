import requests


def main():

    print('===========================')
    print('===== CONSULTA DE CEP =====')
    print('===========================')
    print('')

    cep_input = input('Digite um CEP para consulta: ')

    if len(cep_input) != 8:
        print('Quantidade de digitos inválida.')
        exit()

    link = 'https://viacep.com.br/ws/{}/json/'.format(cep_input)
    r = requests.get(link)

    dic_r = r.json()

    if 'erro' not in dic_r:
        print('==> CEP ENCONTRADO <==\n')

        print('CEP: {}'.format(dic_r['cep']))
        print('Logradouro: {}'.format(dic_r['logradouro']))
        print('Bairro: {}'.format(dic_r['bairro']))
        print('Cidade: {}'.format(dic_r['localidade']))
        print('Estado: {}'.format(dic_r['uf']))
        print('')
    else:
        print('CEP: {} inválido.\n'.format(cep_input))

    op = int(input('Deseja realizar uma nova consulta?\n 1 - SIM  2 - SAIR\n'))

    if op == 1:
        main()
    else:
        print('Saindo... Até logo.')


if __name__ == '__main__':
    main()
