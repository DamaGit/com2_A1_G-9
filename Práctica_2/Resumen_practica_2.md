# Resumen Práctica II 📡

## Objetivos 🎯

• Identificar y caracterizar la **Densidad Espectral de Potencia (PSD)** de señales binarias bipolares, ruido blanco y fuentes reales (imagen y audio) mediante GNU Radio.

• Analizar el impacto del parámetro ***Samples per Symbol* (SPS)** en el ancho de banda, la resolución espectral y la forma de los lóbulos del espectro.

• Validar teóricamente las **limitaciones prácticas** en el análisis espectral de señales con ancho de banda teóricamente infinito, considerando restricciones de muestreo y procesamiento.

## Desarrollo de la práctica 🔬

Mediante la herramienta **GNU Radio Companion** se implementó un flujograma para generar y analizar señales binarias bipolares, ruido blanco y fuentes reales (imagen y audio), evaluando su Densidad Espectral de Potencia (PSD) bajo diferentes configuraciones.

### **Señal Binaria Bipolar** 📊
- La PSD sigue una forma $\text{sinc}^2(f)$, típica de pulsos rectangulares.
- Al aumentar el SPS, el lóbulo principal se estrecha y los lóbulos laterales se acercan, mejorando la resolución espectral.
- El ancho de banda se mantiene constante en aproximadamente 32 kHz, mientras que la frecuencia de muestreo aumenta proporcionalmente al SPS.

### **Ruido Blanco** 🎲
- Presenta una PSD teóricamente plana en todas las frecuencias.
- En la práctica, su ancho de banda está limitado por las restricciones del sistema, observándose una PSD constante dentro de un rango específico.

### **Fuentes Reales** 🎵🖼️
- Las señales de **audio** concentran su PSD en bandas bajas y medias.
- Las señales de **imagen** exhiben un espectro más disperso debido a su mayor complejidad frecuencial.

### **Modificaciones y Codificaciones** ⚙️
- Se realizaron ajustes en el vector $h$ y en bloques como *Constant Source* y *Multiply Const* para generar:
  - Formas de onda personalizadas (diente de sierra 🔸, latidos del corazón ❤️)
  - Modulaciones digitales (OOK, BPSK, ASK, Unipolar RZ, Manchester NRZ)

## Conclusiones Clave 💡

- El aumento del **SPS** mejora la resolución temporal y espectral, pero incrementa el ancho de banda observado.
- Las **limitaciones prácticas** de GNU Radio confinan la PSD a un rango finito, a diferencia del ancho de banda teóricamente infinito de señales ideales.
- El bloque ***Throttle*** regula la tasa de muestreo para evitar el consumo excesivo de recursos computacionales.
- Las **codificaciones de línea** presentan distribuciones espectrales diferentes: Unipolar RZ concentra potencia en bajas frecuencias, mientras Manchester NRZ mitiga la componente DC.
