import climbing_cams as cams
import matplotlib as mpl
import pytest


def test_rack_barchart_fail():
    with pytest.raises(Exception) as e_info:
        cams.plots.rack_barchart(1)
    assert str(e_info.value) == f'{cams.plots.rack_barchart} must be called with a {cams.rack.Rack} ' + \
                                f'instance but it was called with {int}'


def test_racks_barchart_fail():
    with pytest.raises(Exception) as e_info:
        cams.plots.racks_barchart([1])
    assert str(e_info.value) == f'{cams.plots.racks_barchart} must be called with a list of {cams.rack.Rack} ' + \
                                f'but it was called with a list of {int}'


def test_rack_barchart():
    rack = cams.db.select(name="C4")
    fig, ax = cams.plots.rack_barchart(rack)
    assert type(fig) == mpl.figure.Figure
    assert type(ax) == mpl.axes._axes.Axes


def test_racks_barchart():
    racks = [cams.db.select(**spec) for spec in [{'name': 'C4'}, {'name': 'UL'}]]
    assert len(racks) == 2
    fig, ax = cams.plots.racks_barchart(racks)
    assert type(fig) == mpl.figure.Figure
    assert len(ax) == 2


def test_scatter_individual():
    racks = [cams.db.select(**spec) for spec in [{'name': 'C4'}, {'name': 'UL'}]]
    assert len(racks) == 2
    fig, ax = cams.plots.scatter_individual(racks, 'avg', 'weight')
    assert type(fig) == mpl.figure.Figure
    assert type(ax) == mpl.axes._axes.Axes


def test_scatter_average():
    racks = [cams.db.select(**spec) for spec in [{'name': 'C4'}, {'name': 'UL'}]]
    assert len(racks) == 2
    fig, ax = cams.plots.scatter_average(racks, 'avg', 'weight')
    assert type(fig) == mpl.figure.Figure
    assert type(ax) == mpl.axes._axes.Axes

