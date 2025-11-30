from collections import defaultdict
from typing import NamedTuple
from datetime import date, datetime
import csv

Reserva = NamedTuple("Reserva", 
                     [("nombre", str),
                      ("dni", str),
                      ("fecha_entrada", date),
                      ("fecha_salida", date),
                      ("tipo_habitacion", str),
                      ("num_personas", int),
                      ("precio_noche", float),
                      ("servicios_adicionales", list[str])
                    ])


#APARTADO 1

def lee_reservas(fichero:str)->list[Reserva]:
    with open(fichero, encoding = "utf-8") as f:
        lista = []
        lector = csv.reader(f)
        next(lector)
        for nombres, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales in lector:
            fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d").date()
            fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d").date()
            num_personas = int(num_personas)
            precio_noche = float(precio_noche)
            servicios_adicionales = parsea_servicios(servicios_adicionales)
            reservas = Reserva(nombres, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales)
            lista.append(reservas)
    return lista        
    
def parsea_servicios(lista_servicios:str)->list[Reserva]:
        lista = []
        partes = lista_servicios.split(",")
        lista.append(partes)
    
        return lista
        

#APARTADO 2
def total_facturado(reservas: list[Reserva], 
                    fecha_ini: date | None = None, 
                    fecha_fin: date | None = None) -> float:

    facturado = 0
    for e in reservas:
        if fecha_ini <= e.fecha_entrada and fecha_fin>=e.fecha_salida:
            dias = (e.fecha_salida-e.fecha_entrada).days
            facturado += (e.precio_noche*dias)
        else:
            None
    return facturado


#APARTADO 3
def reservas_mas_largas(reservas: list[Reserva], n: int = 3) -> list[tuple[str, date]]:
    lista = []
    for e in reservas:
        duracion=(e.fecha_salida-e.fecha_entrada).days
        lista.append((duracion,e.nombre,e.fecha_entrada))
    lista.sort(reverse=True)

    return [(e[1],e[-1]) for e in lista[:n]]

#APARTADO 4       


def cliente_mayor_facturacion(reservas: list[Reserva], servicios: set[str] | None = None) -> tuple[str, float]:
    
    facturacion_por_cliente = defaultdict(float)
    for reserva in reservas:
        cumple_el_filtro = (servicios is None) or any(s in reserva.servicios_adicionales for s in servicios)
        if cumple_el_filtro:
            facturacion_por_cliente[reserva.dni] += total_facturacion(reserva)
    if not facturacion_por_cliente:
        return ("", 0.0)
    return max(facturacion_por_cliente.items(), key=lambda item: item[1])
        
def total_facturacion(reserva:Reserva) -> float:
    return reserva.precio_noche* (reserva.fecha_salida-reserva.fecha_entrada).days           