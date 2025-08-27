import numpy as np
from gnuradio import gr

class ECG_Block(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name='ECG_Simulation_Block',   # Nombre del bloque
            in_sig=[np.float32],           # Tipo de señal de entrada (puede ser un solo canal de float32)
            out_sig=[np.float32]           # Tipo de señal de salida (ECG)
        )
    
    def work(self, input_items, output_items):
        # Crear un vector de tiempo para la simulación
        t = np.linspace(0, 1, len(input_items[0]))  # Asumimos que input_items tiene la misma longitud para la entrada y salida

        # Simulamos las ondas P, QRS y T usando una combinación de senos y funciones gaussianas
        qrs = np.exp(-0.5 * ((t - 0.4) / 0.1)**2)  # Pico QRS centrado en t=0.4 segundos
        p_wave = 0.5 * np.sin(2 * np.pi * 1 * t)  # Onda P a 1 Hz
        t_wave = 0.8 * np.sin(2 * np.pi * 0.25 * t)  # Onda T a 0.25 Hz

        # Generamos la señal de ECG sumando estas tres ondas
        ecg_signal = p_wave + qrs + t_wave

        # Ajustamos el rango de la señal a -3 a 3
        ecg_signal = ecg_signal / np.max(np.abs(ecg_signal)) * 3
        
        # Asignamos la señal de ECG a la salida
        output_items[0][:] = ecg_signal
        
        return len(output_items[0])
