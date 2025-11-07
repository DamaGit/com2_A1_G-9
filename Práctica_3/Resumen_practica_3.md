# Resumen Práctica III 📡

## Objetivos 🎯

• Producir combinaciones de bloques en **GNU Radio** para la aplicación específica de la **envolvente compleja**.

• Comprender los bloques, diagramas y su funcionalidad para la producción de otros sistemas de comunicación.

• Representar las señales de salida tanto de **RF como en envolvente compleja** en GNU Radio.

## Desarrollo de la práctica 🔬

Se implementaron y analizaron tres modulaciones digitales fundamentales mediante GNU Radio Companion, comparando sus representaciones en RF y envolvente compleja.

### **Modulación OOK (On-Off Keying)** 🔛
- **Concepto**: Modulación por amplitud donde el bit **1** transmite una portadora de amplitud A y el bit **0** no transmite señal.
- **Características**:
  - Constelación unidimensional: puntos en (0,0) y (A,0)
  - Simple de implementar pero sensible al ruido
  - Utilizada en controles remotos y comunicaciones ópticas

### **Modulación BPSK (Binary Phase-Shift Keying)** 🔄
- **Concepto**: Modulación por fase con dos estados separados por 180°
- **Características**:
  - Alta inmunidad al ruido
  - Constelación con puntos en (1,0) y (-1,0)
  - Espectro con forma sine² y simetría perfecta alrededor de fc
  - Utilizada en sistemas satélitales y comunicaciones inalámbricas

### **Modulación FSK (Frequency-Shift Keying)** 📊
- **Concepto**: Modulación por frecuencia donde cada bit se asocia con una frecuencia diferente
- **Características**:
  - Resistente al ruido e interferencias
  - Ancho de banda determinado por la regla de Carson: \( B \approx 2(\Delta f + R_b) \)
  - Requiere cumplir condición de ortogonalidad para constelaciones definidas

### **Implementación de Bloques Personalizados** ⚙️
- **CE VCO**: Genera señal compleja en banda base: \( y[n] = A[n] \cdot e^{jQ[n]} \)
- **RF VCO**: Genera señal real en RF: \( y[n] = A[n] \cdot \cos(2\pi f_c n/f_s + Q[n]) \)
- **Parámetro SPS crítico**: Determina la calidad de representación y evita aliasing

## Conclusiones Clave 💡

- La **conversión RF a envolvente compleja** facilita el procesamiento digital en banda base, reduciendo la carga computacional.

- **BPSK** demostró mayor robustez frente al ruido comparado con **OOK**, mientras que **FSK** ofrece mejor eficiencia espectral.

- El **cumplimiento de la ortogonalidad** en FSK es esencial para constelaciones óptimas y baja probabilidad de error.

- El **parámetro SPS** es crucial para representar correctamente tanto RF como envolvente compleja, asegurando ancho de banda suficiente y sincronía adecuada.

- La **ubicación estratégica de bloques** (como el Interpolating FIR Filter) afecta directamente el desempeño del sistema de comunicación.
