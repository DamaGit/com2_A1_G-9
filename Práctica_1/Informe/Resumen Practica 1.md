# Resumen Practica I #
## Objetivos específicos

• Identificar los aspectos fundamentales en los sistemas de tiempo real y la radio definida por
software.

• Generar funciones a partir de los bloques de implementación de código y evaluar los resultados
con otros bloques.

• Utilizar los bloques implementados para producir una aplicación específica para señales reales.

## Desarrollo de la práctica
Mediante la herramienta GNU Radio Companion se experimentó con bloques programables, sobre los cuales se implementaron las funciones de **Acumulador** y **Diferenciador**.
### **Acumulador**
Calcula la suma acumulativa de las muestras de entrada en tiempo real. Es el equivalente discreto de una integral en tiempo continuo.
### **Diferenciador**
Calcula la diferencia acumulativa entre bloques. Sin embargo, el código tiene un error y no implementa un diferenciador estándar, puede indentificar los cambios abruptos en las señales.
