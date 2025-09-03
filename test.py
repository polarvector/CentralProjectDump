import numpy as np
import time
import imageio.v2 as imageio
from numpy.linalg import svd, matrix_rank
from numba import jit
import csv

@jit(nopython=True)
def rem_svs(m, E1f, E2f, E3f):
    for j in range(m, min(E1f.shape[0], E1f.shape[1])):
        E1f[j, j] = 0
        E2f[j, j] = 0
        E3f[j, j] = 0
    return E1f, E2f, E3f

@jit(nopython=True)
def process_image(r, g, b, U1, E1, V1, U2, E2, V2, U3, E3, V3, imorg):
    min_pix_dev = np.empty(min(r.shape), dtype=np.float64)
    max_pix_dev = np.empty(min(r.shape), dtype=np.float64)
    
    for i in range(min(r.shape)):
        E1f = np.diag(E1.copy())
        E2f = np.diag(E2.copy())
        E3f = np.diag(E3.copy())

        E1f, E2f, E3f = rem_svs(i, E1f, E2f, E3f)

        r_comp = np.dot(U1, np.dot(E1f, V1))
        g_comp = np.dot(U2, np.dot(E2f, V2))
        b_comp = np.dot(U3, np.dot(E3f, V3))

        imgcomp = np.stack((r_comp, g_comp, b_comp), axis=2)
        newimg = np.clip(imgcomp, 0, 255).astype(np.uint8)

        comp_tensor = imorg.astype(np.int16) - newimg.astype(np.int16)

        max_pix_dev[i] = np.max(comp_tensor)
        min_pix_dev[i] = np.min(comp_tensor)
    
    return min_pix_dev, max_pix_dev

def compression_analysis(name):
    start_time = time.time()
    
    imorg = imageio.imread(name)
    
    # Check if the image has an alpha channel and remove it
    if imorg.shape[2] == 4:
        imorg = imorg[:, :, :3]
    
    img = imorg.astype(np.float64)
    
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]
    
    oldranks = [matrix_rank(r), matrix_rank(g), matrix_rank(b)]
    
    U1, E1, V1 = svd(r, full_matrices=False)
    U2, E2, V2 = svd(g, full_matrices=False)
    U3, E3, V3 = svd(b, full_matrices=False)

    min_pix_dev, max_pix_dev = process_image(r, g, b, U1, E1, V1, U2, E2, V2, U3, E3, V3, imorg)
    
    imp_params = np.array([min_pix_dev, max_pix_dev]).T
    
    with open('pixel_deviation.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Singular Value Index", "Min Pixel Deviation", "Max Pixel Deviation"])
        for i, (min_dev, max_dev) in enumerate(imp_params):
            writer.writerow([i, min_dev, max_dev])
    
    print(f"Execution time: {time.time() - start_time} seconds")

# Example usage
compression_analysis('thot.png')
