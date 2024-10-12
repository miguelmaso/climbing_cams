import climbing_cams as cams
import pytest

tol = 1e-4


def create_rack() -> cams.rack.Rack:
    rack = cams.rack.Rack()
    rack.append(cams.cam.Cam('Totem', 'Cam', 1, 'purple', 20.9, 34.2, 95, 10))
    rack.append(cams.cam.Cam('Totem', 'Cam', 1.25, 'green', 25.7, 42.3, 109, 13))
    return rack


def create_rack_2():
    rack = create_rack()
    rack.append(cams.cam.Cam('BD', 'C4', 1, 'red', 30.2, 52.1, 101, 12))
    return rack


def create_rack_3():
    rack = create_rack_2()
    rack.append(cams.cam.Cam('BD', 'UL', 2, 'yellow', 37.2, 64.9, 126, 12))
    return rack


def test_rack():
    rack = create_rack()
    assert len(rack) == 2


def test_rack_name():
    rack = create_rack()
    assert rack.name() == 'Totem Cam'


def test_rack_name_2():
    rack = create_rack_2()
    assert rack.name() == 'Totem Cam | BD C4'


def test_rack_name_3():
    rack = create_rack_3()
    assert rack.name() == 'Totem Cam | BD C4 | BD UL'


def test_rack_properties():
    rack = create_rack()
    assert rack.min == 20.9
    assert rack.max == 42.3
    assert rack.avg == pytest.approx(30.775, tol)
    assert rack.specific_weight == pytest.approx(6.855, tol)
    assert rack.weight == 204
    assert rack.min_strength == 10
    assert rack.max_strength == 13
    assert rack.expansion_rate == pytest.approx(1.641, tol)
    assert rack.expansion_range == pytest.approx(14.95, tol)
