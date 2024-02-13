from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np


def allign(file):
    data = fits.open(file)
    hdu = data[0]
    startt = hdu.header['CRVAL1']
    size = hdu.header['NAXIS1']
    prwto = hdu.header['CRPIX1']
    step = hdu.header['CDELT1']
    if prwto!=1.:
        prwto=prwto
    elif prwto==1:
        prwto=0
    size = size-prwto #give the right wavelength to the first pixel of the spectrum
    lamda = np.arange(startt,startt+size*step,step) #beginning to end of spectrum
    flux = hdu.data[prwto:]
    data.close()
    return lamda,flux

def plot_spec(lamda,flux):
    plt.figure(figsize=(10,6))
    fig = plt.plot(lamda,flux, '-k')
    return fig


