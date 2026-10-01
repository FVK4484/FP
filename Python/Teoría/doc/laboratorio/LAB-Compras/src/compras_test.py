from compras import*

def lee_compras_test(fichero: str) -> list[Compra]:
    print(f"Número de registros leídos: {len(lee_compras(fichero))}")
    print(f"Tres primeros registros: {lee_compras(fichero)[:3]}")
    print(f"Tres últimos registros: {lee_compras(fichero)[-3:]}")

def compra_maxima_minima_provincia_test(compras: list[Compra], provincia: str) -> tuple[float, float]:
    print(f"Importe máximo de la provincia de {provincia} : {compra_maxima_minima_provincia(compras, provincia)[0]} . Importe mínimo: {compra_maxima_minima_provincia(compras, provincia)[1]}")

def hora_menos_afluencia_test(compras: list[Compra]) -> tuple[time, int]:
    print(f"La hora con menos afluencia es: {hora_menos_afluencia(compras)[0]} h. con {hora_menos_afluencia(compras)[1]} llegadas de clientes")

def supermercados_mas_facturacion_test(compras: list[Compra], n: int = 3) -> list[tuple[int, tuple[str, float]]]:
    print(f"Los {n} supermercados con más facturación son: {supermercados_mas_facturacion(compras, n)}")

def clientes_itinerantes_test(compras: list[Compra], n: int) -> list[tuple[str, list]]:
    print(f"Los clientes itinerantes que han comprado en más de {n} provincias son: {clientes_itinerantes(compras, n)}")

def dias_estrella_test(compras: list[Compra], supermercado: str, provincia: str) -> list[datetime]:
    print(f"Los días estrella del supermercado {supermercado} de la provincia de {provincia} son: {dias_estrella(compras, supermercado, provincia)}")

def main():
    compras = lee_compras(r"doc\laboratorio\LAB-Compras\data\compras.csv")
    # lee_compras_test(r"doc\laboratorio\LAB-Compras\data\compras.csv")
    # compra_maxima_minima_provincia_test(compras, "Huelva")
    # compra_maxima_minima_provincia_test(compras, None)
    # hora_menos_afluencia_test(compras)
    # supermercados_mas_facturacion_test(compras, 2)
    # supermercados_mas_facturacion_test(compras)
    # clientes_itinerantes_test(compras, 7)
    dias_estrella_test(compras,"Aldi", "Huelva")

if __name__ == '__main__':
    main()