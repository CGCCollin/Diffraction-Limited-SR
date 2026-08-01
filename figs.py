import matplotlib.pyplot as plt
import tifffile
import numpy as np

fig, axes = plt.subplots(1,3)
img_1 = tifffile.imread(r"E:\MASC\EE8204\Project\code\dset_out\img_files\CCPs_c1_LR_SNR-1_UNITY_BS-1.0.tif")
img_2 = tifffile.imread(r"E:\MASC\EE8204\Project\code\dset_out\img_files\ER-KDEL_c15_LR_SNR-15_UNITY_BS-1.0.tif")
img_3 = tifffile.imread(r"E:\MASC\EE8204\Project\code\dset_out\img_files\IMM-cox8a_c4_LR_SNR-3_UNITY_BS-1.0.tif")
axes[0].imshow(img_1, vmin = np.percentile(img_1,1), vmax = np.percentile(img_1,99),cmap='grey')
axes[0].set_axis_off()
axes[1].imshow(img_2, vmin = np.percentile(img_2,1), vmax = np.percentile(img_2,99),cmap='grey')
axes[1].set_axis_off()
axes[2].imshow(img_3, vmin = np.percentile(img_3,1), vmax = np.percentile(img_3,99),cmap='grey')
axes[2].set_axis_off()
plt.show()
#Demonstrating tranforms
fig, axes = plt.subplots(2,4)