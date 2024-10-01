import climbing_cams as cams
import pytest

tol = 1e-4


def create_rack():
    rack = cams.rack.Rack()
    rack.append(cams.cam.Cam('Totem', 'Cam', 1, 'purple', 20.9, 34.2, 95, 10))
    rack.append(cams.cam.Cam('Totem', 'Cam', 1.25, 'green', 25.7, 42.3, 109, 13))
    return rack


def test_rack():
    rack = create_rack()
    assert len(rack) == 2
