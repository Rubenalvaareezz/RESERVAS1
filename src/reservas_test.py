from reservas import *
from datetime import datetime, date
fichero = "data/reservas.csv"


reservas = lee_reservas(fichero)
# for e in reservas:
#     print(e)

# fecha_ini = date(2022,2,1)
# fecha_fin = date(2022,2,28)
# facturado = total_facturado(reservas,fecha_ini,fecha_fin)
# print(f"Desde 1 de febrero de 2022 hasta 28 de febrero de 2022: {facturado}")

# #APARTADO 3
# n = reservas_mas_largas(reservas,n=3)
# print(f"Las reservas de mas duracion son: {n}")



if __name__ == "__main__":
    from datetime import date
    from reservas import *
#APARTAO 1
    fichero = "data/reservas.csv"
    reservas = lee_reservas(fichero)

    for e in reservas:
        print(e)
#APARTADO 2
    fecha_ini = date(2022, 2, 1)
    fecha_fin = date(2022, 2, 28)
    facturado = total_facturado(reservas, fecha_ini, fecha_fin)

    print(f"Desde 1 de febrero de 2022 hasta 28 de febrero de 2022: {facturado}")

#APARTADO 3
    n = reservas_mas_largas(reservas,n=3)
    print(f"Las reservas de mas duracion son: {n}")
    
#APARTADO 4
    res = cliente_mayor_facturacion(reservas, {"Spa"})
    print(res)