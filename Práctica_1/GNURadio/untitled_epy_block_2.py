import numpy as np
from gnuradio import gr

class remove_mean(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="remove_mean",
            in_sig=[np.float32],
            out_sig=[np.float32])

    def work(self, input_items, output_items):
        x = input_items[0]
        output_items[0][:] = x - np.mean(x)
        return len(output_items[0])
