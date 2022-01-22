import numpy as np
from numpngw import write_apng

# Example 5
#
# Create an 8-bit RGB animated PNG file.

height = 20
width = 200
t = np.linspace(0, 15*np.pi, width)
seq = []
for phase in np.linspace(0, 2*np.pi, 25, endpoint=False):
    y = 250*0.5*(1 + np.sin(t - phase))
    a = np.zeros((height, width, 3), dtype=np.uint8)
    a[:, :, 0] = y
    a[:, :, 2] = y
    seq.append(a)
    
print seq

write_apng("example5.png", seq, delay=50, use_palette=True)
