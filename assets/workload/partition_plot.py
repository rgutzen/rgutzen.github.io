import matplotlib.pyplot as plt  # 3.1.2
import seaborn as sns  # 0.9.0
import pandas as pd  # 0.25.3
import numpy as np  # 1.17.4
import scipy as sc  # 1.3.2

def partition_plot(partitions, xvalues=None, colors=None, kind='cubic', N=200,
                   sigma=1.0, pad=0, ax=None):
    """
    Visualizes partitions over time.

    Parameters
    ----------
    partitions : pands.DataFrame or np.ndarray
        The first axis (rows) is interpreted as the catergories,
        the second axis (columns) is interpreted as a time axis.
    xvalues : np.ndarray (default: None)
        Array of time points for the given partitions. Must be of same length
        as the partition columns.
        If partitions is a DataFrame xvalues are set the columns.
    colors : list (default: None)
        List of colors to fill the partion areas. Must be of same length as
        partitions. If None uses the current color palette.
    kind : str (default: 'cubic')
        Interpolation parameter passed to scipy.interpolate.interp1d()
    N : int (default: 200)
        Number of points to use to draw the interpolated functions.
    sigma : float (default: 1.0)
        Width of kernel used to smooth the interpolated functions in units
        of input partition columns.
    pad : int (default: 0)
        While calculating the partition border functions pad temporarily adds
        x columns with a uniform partition distribution to the left and right
        side of the partition matrix in order to eliminate eventual border
        artefacts.
    ax : matplotlib axis (default: None)
        Axis to draw in the plot. If None, creates a new figure.

    Returns
    -------
    curves : np.ndarray
        Interpolated partition border curves, with shape len(partitions) x N.
    """
    if isinstance(partitions, pd.DataFrame):
        xvalues = partitions.columns.to_numpy()
        labels = partitions.index.to_list()
        partitions = partitions.to_numpy()
    else:
        labels = np.arange(len(partitions))

    Npartitions, Npoints = partitions.shape

    if xvalues is None:
        xvalues = np.arange(Npoints)
    elif not len(xvalues) == Npoints:
        raise Warning('Array of xvalues is not of the correct length!')

    if colors is None:
        colors = sns.color_palette()
    elif not len(colors) == Npartitions:
        raise Warning('List of colors is not of the correct length!')

    if pad:
        partitions = np.concatenate((np.ones((Npartitions,pad)),
                                     partitions,
                                     np.ones((Npartitions,pad))), axis=1)
        xvalues = np.concatenate((np.arange(xvalues[0]-pad,xvalues[0]),
                                  xvalues,
                                  np.arange(xvalues[-1]+1, xvalues[-1]+1+pad)))

    partitions /= np.sum(partitions, axis=0)[np.newaxis, :]
    y = np.cumsum(partitions[:-1], axis=0)
    f = sc.interpolate.interp1d(xvalues, y, kind=kind, axis=1)
    x = np.linspace(xvalues[0], xvalues[-1], N)

    curves = np.concatenate((np.zeros(N)[np.newaxis,:],
                             f(x).clip(0,1),
                             np.ones(N)[np.newaxis,:]),
                            axis=0)

    if sigma:
        s = sigma/Npoints * (N+2*pad)
        win = sc.signal.hann(int(s))
        for i, curve in enumerate(curves[1:-2]):
            curves[i+1] = sc.signal.convolve(curve, win, mode='same')\
                        / sum(win)

    if ax is None:
       fig, ax = plt.subplots()

    for i, curve in enumerate(curves[:-1]):
        if pad:
            ax.fill_between(x[pad:-pad], curve[pad:-pad], 1,
                            color=colors[i], label=label[i])
        else:
            ax.fill_between(x, curve, 1., color=colors[i], label=i)

    ax.set_ylim((0,1))
    if pad:
        return curves[:, pad:-pad]
    else:
        return curves
