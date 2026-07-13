import numpy as np
import pandas as pd
import tifffile
import seaborn as sns
import matplotlib.pyplot as plt
import torch

# img = tifffile.imread(r"dset/CCPs/cell1/SR1.tif")
# flat_data = img.flatten()
# print(flat_data.shape)
# df = pd.DataFrame(columns=["Brightness"],data=flat_data)
# grp = df.groupby("Brightness").count()
# vmin = np.percentile(img, 1)
# vmax = np.percentile(img, 99)
# print(vmin)
# print(vmax)
# plt.imshow(img, vmin=vmin, vmax=vmax)
# plt.legend()
# plt.colorbar(label="intensity")
# plt.show()

val1 = np.random.rand(2, 2)
val2 = np.random.rand(2, 2)

val1 = torch.from_numpy(val1)
val2 = torch.from_numpy(val2)

print(torch.dist(val1, val2, 2))
