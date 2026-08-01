import tifffile
import numpy as np

data = tifffile.imread(r"E:\MASC\EE8204\Project\code\dset_out\img_files\CCPs_c1_LR_SNR-1_VHFLIP_BS-1.0043.tif")
data = data.astype(np.float32)
print(data.max())
print(data.min())

print(data[0][124:128])
print(data.dtype)

d2 = tifffile.imread("E:\MASC\EE8204\Project\code\dset\Microtubules\cell8\SR8.tif")
print(d2.max())
print(d2.min())
print(d2.dtype)