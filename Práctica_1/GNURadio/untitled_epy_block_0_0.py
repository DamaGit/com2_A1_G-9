import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
    def __init__(self, ts=1):  # Agregar 'ts' como parámetro de entrada con valor por defecto 1
        gr.sync_block.__init__(
            self,
            name='e_Dif',   
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.ts = ts  # Guardamos el valor de ts en un atributo de la clase
        self.acum_anterior = 0
        
    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y = output_items[0]  # Señal de salida
        N = len(x)
    
        # Diferenciación acumulada con 'ts' como factor de escala
        for i in range(N):
            y[i] = (x[i] - self.acum_anterior) / self.ts  # Restamos el valor acumulado anterior y dividimos por 'ts'
            self.acum_anterior = x[i]  # Actualizamos el acumulado con el valor actual
        
        return len(y)
