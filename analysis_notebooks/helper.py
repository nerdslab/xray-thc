import numpy as np
from numpy.random import choice
import matplotlib.pyplot as plt

## Train imgs and masks
train_imgs_ctx = np.load('data/imgs_ctx.npz')['arr_0']
train_masks_ctx = np.load('data/masks_ctx.npz')['arr_0']

train_imgs_str = np.load('data/imgs_str.npz')['arr_0']
train_masks_str = np.load('data/masks_str.npz')['arr_0']

train_imgs_trn = np.load('data/imgs_trn.npz')['arr_0']
train_masks_trn = np.load('data/masks_trn.npz')['arr_0']

train_imgs_zi = np.load('data/imgs_zi.npz')['arr_0']
train_masks_zi = np.load('data/masks_zi.npz')['arr_0']

def matrix_rearrange(mat):
	mat_new = np.zeros_like(mat)

	mat_new[0,0] = mat[0,0]
	mat_new[0,1] = mat[0,3]
	mat_new[0,2] = mat[0,1]
	mat_new[0,3] = mat[0,2]

	mat_new[1,0] = mat[3,0]
	mat_new[1,1] = mat[3,3]
	mat_new[1,2] = mat[3,1]
	mat_new[1,3] = mat[3,2]

	mat_new[2,0] = mat[1,0]
	mat_new[2,1] = mat[1,3]
	mat_new[2,2] = mat[1,1]
	mat_new[2,3] = mat[1,2]

	mat_new[3,0] = mat[2,0]
	mat_new[3,1] = mat[2,3]
	mat_new[3,2] = mat[2,1]
	mat_new[3,3] = mat[2,2]

	return mat_new

def plotImgs_masks(im_cc=train_imgs_ctx,im_ss=train_imgs_str,im_tt=train_imgs_trn,im_zz=train_imgs_zi,
                   mk_cc=train_masks_ctx,mk_ss=train_masks_str,mk_tt=train_masks_trn,mk_zz=train_masks_zi):
    
    cc = choice(32,1)
    ss = choice(32,1)
    tt = choice(32,1)
    zz = choice(32,1)
    
    ff = plt.figure(figsize=(12,6))
    
    plt.subplot(241)
    plt.imshow(np.squeeze(im_cc[cc]),cmap='gray')
    plt.axis('off')
    plt.title('CTX Img')
    plt.subplot(242)
    plt.imshow(np.squeeze(im_ss[ss]),cmap='gray')
    plt.axis('off')
    plt.title('STR Img')
    plt.subplot(243)
    plt.imshow(np.squeeze(im_tt[tt]),cmap='gray')
    plt.axis('off')
    plt.title('TRN Img')
    plt.subplot(244)
    plt.imshow(np.squeeze(im_zz[zz]),cmap='gray')
    plt.axis('off')
    plt.title('ZI Img')
    
    plt.subplot(245)
    plt.imshow(np.squeeze(mk_cc[cc]),cmap='gray')
    plt.axis('off')
    plt.title('CTX Mask')
    plt.subplot(246)
    plt.imshow(np.squeeze(mk_ss[ss]),cmap='gray')
    plt.axis('off')
    plt.title('STR Mask')
    plt.subplot(247)
    plt.imshow(np.squeeze(mk_tt[tt]),cmap='gray')
    plt.axis('off')
    plt.title('TRN Mask')
    plt.subplot(248)
    plt.imshow(np.squeeze(mk_zz[zz]),cmap='gray')
    plt.axis('off')
    plt.title('ZI Mask')