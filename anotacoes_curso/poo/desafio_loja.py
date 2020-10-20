from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    cliente = Cliente('Maria Lima', 44)
    vendedor = Vendedor('Pedro Garrido', 36, 5000)
    compra1 = Compra(vendedor, datetime.now(), 512)
    compra2 = Compra(vendedor, datetime(2020, 7, 15), 256)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f'Total: {valor_total} em {qtde_compras} compras')
    print(f'Última compra: {cliente.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
