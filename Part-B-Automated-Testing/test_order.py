
import pytest

from order import (
    calculate_discount,
    calculate_shipping,
    calculate_order_total
)


# ==========================================
# TESTS FOR DISCOUNT CALCULATION
# ==========================================

def test_calculate_discount_with_valid_percentage():
    assert calculate_discount(5000, 10) == 4500.0


def test_calculate_discount_with_zero_percent():
    assert calculate_discount(5000, 0) == 5000.0


def test_calculate_discount_with_full_percentage():
    assert calculate_discount(5000, 100) == 0.0


def test_calculate_discount_with_negative_total():
    with pytest.raises(ValueError):
        calculate_discount(-5000, 10)


def test_calculate_discount_with_percentage_above_limit():
    with pytest.raises(ValueError):
        calculate_discount(5000, 110)


def test_calculate_discount_with_negative_percentage():
    with pytest.raises(ValueError):
        calculate_discount(5000, -5)


# ==========================================
# TESTS FOR SHIPPING CALCULATION
# ==========================================

def test_calculate_shipping_below_free_shipping_limit():
    assert calculate_shipping(49999.99) == 2500.0


def test_calculate_shipping_at_free_shipping_limit():
    assert calculate_shipping(50000) == 0.0


def test_calculate_shipping_above_free_shipping_limit():
    assert calculate_shipping(50000.01) == 0.0


def test_calculate_shipping_with_zero_subtotal():
    assert calculate_shipping(0) == 2500.0


def test_calculate_shipping_with_negative_subtotal():
    with pytest.raises(ValueError):
        calculate_shipping(-100)


# ==========================================
# TESTS FOR COMPLETE ORDER CALCULATION
# ==========================================

def test_calculate_order_total_without_discount():
    assert calculate_order_total(5000, 2) == 12500.0


def test_calculate_order_total_with_discount():
    assert calculate_order_total(5000, 2, 10) == 11500.0


def test_calculate_order_total_with_free_shipping():
    assert calculate_order_total(30000, 2) == 60000.0


def test_calculate_order_total_with_zero_quantity():
    with pytest.raises(ValueError):
        calculate_order_total(5000, 0)


def test_calculate_order_total_with_negative_unit_price():
    with pytest.raises(ValueError):
        calculate_order_total(-5000, 2)


# ==========================================
# ADDITIONAL COMBINED-PATH TESTS
# ==========================================

def test_order_with_full_discount_and_shipping():
    assert calculate_order_total(5000, 1, 100) == 2500.0


def test_order_with_discount_qualifying_for_free_shipping():
    assert calculate_order_total(30000, 2, 10) == 54000.0


def test_order_rejects_invalid_discount_percentage():
    with pytest.raises(ValueError):
        calculate_order_total(5000, 2, 110)
