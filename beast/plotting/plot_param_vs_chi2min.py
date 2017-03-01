#!/usr/bin/env python
"""
Plot the chi2min versus the fit parametrs
Used to explore where the bad (and good) fits are located
"""

from __future__ import print_function

import matplotlib.pyplot as plt
from astropy.table import Table
from matplotlib.colors import LogNorm
from matplotlib import rc

# local imports
from beastplotlib import (fancify_colname, initialize_parser,
                          plot_generic, set_params)

def make_param_vs_chi2min_plots(statsfile, suffix='Exp', figsize=(20,10)):
    '''Makes a set of 6 diagnostic 2D histograms for BEAST output.

    Parameters
    ----------
    statsfile : str, file-like, list, pathlib.Path object
        File with BEAST output; see astropy.io.ascii.read docs for full 
        description of allowed input types.
    suffix : str, optional
        Column type ('Exp', 'Best', 'p16', 'p50', 'p84').
        Defaults to 'Exp'.
    figsize : tuple of ints, optional
        Size of figure to return in inches (width, height).
        Defaults to (10, 5.5).

    Returns
    -------
    fig : matplotlib figure object
        Figure with diagnostic plots
    '''
    stats = Table.read(statsfile)

    base_cnames = ['Av', 'logA', 'M_ini', 'Rv', 'f_A', 'Z']
    cnames = ['{}_{}'.format(n, suffix) for n in base_cnames]
    ycol = 'chi2min'
    plot_pairs = [[cnames[0], ycol],
                  [cnames[1], ycol],
                  [cnames[2], ycol],
                  [cnames[3], ycol],
                  [cnames[4], ycol],
                  [cnames[5], ycol]]
    xlog_decide = [False, False, True, False, False, False]
    fig, axes = plt.subplots(2, 3, figsize=figsize)
    ax = axes.ravel()
    for i, pair in enumerate(plot_pairs):
        plot_generic(stats, pair[0], pair[1], fig, ax[i],
                     xlog=xlog_decide[i],ylog=True,
                     plot_kwargs={'norm':LogNorm()})
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    parser = initialize_parser()
    parser.add_argument('filename', type=str,
                        help='Path to FITS file with output stats')
    suffixes = ['Exp', 'Best', 'p50']
    parser.add_argument('--suffix', action='store', default='Exp',
                        choices=suffixes,
                        help='Choose column type to plot. \
                        Must be one of: "{}"'.format('", "'.join(suffixes))
                        )
    args = parser.parse_args()
    if args.tex:
        plt.rc({'usetex':True})
    basename = args.filename.replace('.fits', '_diagnostics')

    set_params(lw=2, fontsize=16, usetex=False)
    fig = make_param_vs_chi2min_plots(args.filename, suffix=args.suffix)

    if args.savefig:
        fig.savefig('{}.{}'.format(basename, args.savefig))
    else:
        plt.show()
