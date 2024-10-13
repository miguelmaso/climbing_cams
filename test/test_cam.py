import climbing_cams as cams
import pytest

tol = 1e-4


def create_cam():
    return cams.cam.Cam('Totem', 'Cam', 1.25, 'green', 25.7, 42.3, 109, 13)


def test_cam_eq():
    a = create_cam()
    b = create_cam()
    assert a == b


def test_cam_si():
    cam = create_cam()
    assert cam.brand == 'Totem'
    assert cam.name == 'Cam'
    assert cam.number == 1.25
    assert cam.color == 'green'
    assert cam.min == 25.7
    assert cam.max == 42.3
    assert cam.weight == 109
    assert cam.strength == 13


def test_cam_imp():
    cams.units.Measurements.set_system(cams.units.System.IMPERIAL)
    cam = create_cam()
    assert cam.brand == 'Totem'
    assert cam.name == 'Cam'
    assert cam.number == 1.25
    assert cam.color == 'green'
    assert cam.min == pytest.approx(1.0118, tol)
    assert cam.max == pytest.approx(1.6654, tol)
    assert cam.weight == pytest.approx(0.2403, tol)
    assert cam.strength == 13


def test_cam_secondary_properties():
    cams.units.Measurements.set_system(cams.units.System.INTERNATIONAL)
    cam = create_cam()
    assert cam.range == [25.7, 42.3]
    assert cam.expansion_rate == pytest.approx(1.6459, tol)
    assert cam.expansion_range == pytest.approx(16.6, tol)
    assert cam.specific_weight == pytest.approx(6.5663, tol)
    assert cam.avg == pytest.approx(34, tol)


def test_cam_create_2(capsys):
    cam = cams.cam.Cam('Totem', 'Cam', 1.25, 'green', 42.3, 25.7, 109, 13)
    captured = capsys.readouterr()
    assert cam.min == 25.7
    assert cam.max == 42.3
    assert captured.out == 'The cam Totem Cam [1.25] has been defined with a negative range. New range:\n' + \
                           'min: 25.7\n' + \
                           'max: 42.3\n'
