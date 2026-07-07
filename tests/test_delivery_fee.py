import pytest
from delivery_fee import calculate_delivery_fee


def test_calculate_delivery_fee_basic():
    """3 km de distância: 5.0 + (1.5 * 3) = 9.5"""
    assert calculate_delivery_fee(distance_km=3, order_total=40.0) == 9.5


def test_calculate_delivery_fee_zero_distance():
    """Distância zero: cobra apenas a taxa base"""
    assert calculate_delivery_fee(distance_km=0, order_total=20.0) == 5.0


def test_calculate_delivery_fee_free_shipping():
    """Pedido acima de R$ 100 tem frete grátis, independente da distância"""
    assert calculate_delivery_fee(distance_km=10, order_total=150.0) == 0.0


def test_calculate_delivery_fee_free_shipping_boundary():
    """Pedido exatamente em R$ 100 também tem frete grátis"""
    assert calculate_delivery_fee(distance_km=5, order_total=100.0) == 0.0


def test_calculate_delivery_fee_negative_distance_raises_error():
    with pytest.raises(ValueError):
        calculate_delivery_fee(distance_km=-1, order_total=30.0)


def test_calculate_delivery_fee_negative_order_total_raises_error():
    with pytest.raises(ValueError):
        calculate_delivery_fee(distance_km=2, order_total=-10.0)