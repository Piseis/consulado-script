# Script para sacar cita en el consulado de España

## Descripción
El script va a checkear cada 1 min la url del consulado de España. Si la url redirecciona al consulado, el script esperará q min más y seguirá repitiendo el proceso. En caso de redireccionar para sacar cita para pasaporte sonara una notificación y se detendrá el script.

#

## Para instalar y correr el script
1. Ejecutar el siguiente comando para instalar las dependencias: 
```
pip install -r requirements.txt
```
2. Para ejecutar el proyecto:
```
python main.py
```