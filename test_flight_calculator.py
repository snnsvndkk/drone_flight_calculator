import pytest
from flight_calculator import calculate_flight_time


def test_calculate_flight_time_zero_weight_returns_full_time():
    assert calculate_flight_time(0) == 180


def test_calculate_flight_time_reduces_with_weight():
    assert calculate_flight_time(100) == 170
    assert calculate_flight_time(500) == 130


def test_calculate_flight_time_clamps_to_zero():
    assert calculate_flight_time(1800) == 0
    assert calculate_flight_time(2000) == 0


def test_calculate_flight_time_negative_weight_raises_value_error():
    with pytest.raises(ValueError, match="Payload weight cannot be negative."):
        calculate_flight_time(-1)