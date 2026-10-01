from typing import Dict, List, NamedTuple, Tuple 
from datetime import date 
import csv
from datetime import*
from collections import Counter, defaultdict
 
IntervaloFechas = NamedTuple("IntervaloFechas",  
                     [("inicio", date), ("fin", date)]) 
 
Factura = NamedTuple("Factura",  
                     [("id_vivienda", str), 
                      ("tipo_vivienda", str), 
                      ("barrio", str), 
                      ("tipo_tarifa", str), 
                      ("periodo_facturado", IntervaloFechas), 
                      ("coste_potencia", float), 
                      ("consumo_punta", float), 
                      ("consumo_valle", float), 
                      ("precio_punta", float), 
                      ("precio_valle", float), 
                      ("importe_total", float)])

# Ejercicio 1

def lee_facturas(ruta_fichero: str) -> List[Factura]:
    lista = []
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for id_vivienda, tipo_vivienda, barrio, tipo_tarifa, periodo_inicio, periodo_fin, coste_potencia, consumo_punta, consumo_valle, precio_kwh, importe_total in lector:
            periodo_inicio = parsea_fecha(periodo_inicio)
            periodo_fin = parsea_fecha(periodo_fin)
            periodo_facturado = IntervaloFechas(periodo_inicio, periodo_fin)
            coste_potencia = float(coste_potencia)
            consumo_punta = float(consumo_punta)
            consumo_valle = float(consumo_valle)
            if tipo_tarifa == 'única':
                precio_punta = precio_valle = float(precio_kwh)
            else:
                precio_punta, precio_valle = [float(precio) for precio in precio_kwh.split("/")]
            importe_total = float(importe_total)
            tupla = Factura(id_vivienda, tipo_vivienda, barrio, tipo_tarifa, periodo_facturado, coste_potencia, consumo_punta, consumo_valle, precio_punta, precio_valle, importe_total)
            lista.append(tupla)
        return sorted(lista, key = lambda x:x.periodo_facturado.inicio)
    
def parsea_fecha(fecha: str) -> date:
    return datetime.strptime(fecha, '%Y-%m-%d').date()

# Ejercicio 2

def extrae_precio_por_mes(facturas: List[Factura], tipo_tarifa: str) -> Dict[str, Tuple[float, float]]:
    dicc = defaultdict(list)
    for factura in facturas:
        if factura.tipo_tarifa == tipo_tarifa:
            mes = factura.periodo_facturado.inicio.strftime("%Y-%m")
            dicc[mes] = (factura.precio_punta, factura.precio_valle)
    return dicc

def busca_vivienda_mayor_consumo_acumulado(facturas: List[Factura]) -> Tuple[str, float]:
    dicc = defaultdict(float)
    for factura in facturas:
        dicc[factura.id_vivienda] += factura.consumo_punta + factura.consumo_valle
    return max(dicc.items(), key = lambda x:x[1])

def barrios_mayor_consumo_valle_medio(facturas: List[Factura], top_n: int) -> List[str]:
    dicc1 = defaultdict(float)
    dicc2 = defaultdict(int)
    for factura in facturas:
        dicc1[factura.barrio] += factura.consumo_valle
        dicc2[factura.barrio] += 1
    for consumo in dicc1:
        dicc1[consumo] /= dicc2[consumo]

    return [barrio for barrio, _ in sorted(dicc1.items(), key = lambda x:x[1], reverse = True)[:top_n]]

print(barrios_mayor_consumo_valle_medio(lee_facturas(r'FP_25_26\doc\examenes\Exámenes-curso-2023-2024\Examen-de-la-primera-convocatoria-(junio2024)\data\consumos_sevilla_2023.csv'), 3))

