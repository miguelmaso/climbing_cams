import matplotlib.pyplot as plt
from .units import Measurements


def plot_ranges(racks, smart_ylabels=True, numbers_inside=True):
    sizes = [len(rack) for rack in racks]
    fig, axes = plt.subplots(nrows=len(racks), sharex=True,
                             gridspec_kw={'height_ratios': sizes, 'hspace': 0})
    axes = [axes] if len(racks) == 1 else axes

    for rack, ax in zip(racks, axes):
        rack.plot_bar_chart(ax, number_inside=numbers_inside)
        sep = '\n'
        ax.set_ylabel(f'{rack.name(sep)}')
        ax.spines.right.set_visible(False)
        ax.spines.left.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.tick_params(length=0)
        ax.xaxis.grid()
        ax.set_axisbelow(True)
        if smart_ylabels:
            ax.set_yticklabels([])
            ax.set_ylabel(f'{rack.name(sep)}', rotation=0, horizontalalignment='right', verticalalignment='center')
    fig.tight_layout()
    return fig, axes


def scatter_average(racks, xvalue, yvalue, ax=None):
    if not ax:
        fig, ax = plt.subplots()
    else:
        fig = ax.get_figure()
    for rack in racks:
        ax.plot([getattr(rack, xvalue)], [getattr(rack, yvalue)],
                label=rack.name(), marker='o', markersize=10, linewidth=0, alpha=.7)
        ax.legend()
    ax.set_xlabel(f'{xvalue.replace("_", " ").capitalize()} [{Measurements.get_label(xvalue)}]')
    ax.set_ylabel(f'{yvalue.replace("_", " ").capitalize()} [{Measurements.get_label(yvalue)}]')
    fig.tight_layout()
    return fig, ax


def scatter_individual(racks, xvalue, yvalue, ax=None):
    if not ax:
        fig, ax = plt.subplots()
    else:
        fig = ax.get_figure()
    for rack in racks:
        x = [getattr(i, xvalue) for i in rack]
        y = [getattr(i, yvalue) for i in rack]
        ax.plot(x, y, label=rack.name(), marker='o', markersize=10, linewidth=0, alpha=.7)
        ax.legend()
    ax.set_xlabel(f'{xvalue.replace("_", " ").capitalize()} [{Measurements.get_label(xvalue)}]')
    ax.set_ylabel(f'{yvalue.replace("_", " ").capitalize()} [{Measurements.get_label(yvalue)}]')
    fig.tight_layout()
    return fig, ax
