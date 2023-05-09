import pickle
from collections import Counter

with open('traficoweb.log', 'r') as archivo:
    lineas = archivo.readlines()


registros = []
for i in range(0, len(lineas), 8):
    registro = {}
    registro['ip'] = lineas[i].strip().split(': ')[1]
    registro['fecha'] = lineas[i+1].strip().split(': ')[1]
    registro['metodo'] = lineas[i+2].strip().split(': ')[1]
    registro['url'] = lineas[i+3].strip().split(': ')[1]
    registro['codigo'] = lineas[i+4].strip().split(': ')[1]
    registro['tamaño'] = lineas[i+5].strip().split(': ')[1]
    registros.append(registro)

with open('archivo.pickle', 'wb') as archivo:
    pickle.dump(registros, archivo)

with open("traficoweb.log", "rb") as archivo:
    registros = pickle.load(archivo)

total_solicitudes = len(registros)

metodos = [registro["Método"] for registro in registros]
solicitudes_por_metodo = Counter(metodos)

codigos_respuesta = [registro["Código de respuesta"] for registro in registros]
solicitudes_por_codigo = Counter(codigos_respuesta)

tamanio_total = sum(registro["Tamaño de respuesta"] for registro in registros)

if total_solicitudes > 0:
    tamanio_promedio = tamanio_total / total_solicitudes
else:
    tamanio_promedio = 0

urls = [registro["URL"] for registro in registros]
solicitudes_por_url = Counter(urls)

print("Número total de solicitudes recibidas:", total_solicitudes)
print("Número de solicitudes por método HTTP:", solicitudes_por_metodo)
print("Número de solicitudes por código de respuesta:", solicitudes_por_codigo)
print("Tamaño total de respuesta:", tamanio_total)
print("Tamaño promedio de respuesta por solicitud:", tamanio_promedio)
print("Las 10 URL más solicitadas, con el número de solicitudes:")
