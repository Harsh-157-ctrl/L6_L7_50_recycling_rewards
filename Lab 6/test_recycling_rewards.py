import pytest
from recycling_rewards import reward_points, collection_accepted, slot_status

# --- Tests for reward_points ---

def test_reward_points_unknown_material():
    with pytest.raises(ValueError, match="unknown material"):
        reward_points("glass", 10, False)

def test_reward_points_invalid_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        reward_points("paper", -1, False)

def test_reward_points_below_minimum():
    assert reward_points("paper", 3, False) == 0

def test_reward_points_bonus_non_metal():
    assert reward_points("paper", 10, True) == 36

def test_reward_points_metal_large_weight_with_bonus():
    assert reward_points("metal", 30, True) == 504

def test_reward_points_plastic_large_weight_no_bonus():
    assert reward_points("plastic", 30, False) == 270


# --- Tests for collection_accepted ---

def test_collection_hazardous_within_limit():
    assert collection_accepted(4, 2, True) is True

def test_collection_hazardous_over_limit():
    assert collection_accepted(6, 2, True) is False

def test_collection_overweight_non_hazardous():
    assert collection_accepted(60, 2, False) is False

def test_collection_accepted_standard():
    assert collection_accepted(20, 2, False) is True

def test_collection_too_many_bags():
    assert collection_accepted(20, 5, False) is False


# --- Tests for slot_status ---

def test_slot_status_morning_holiday_late():
    assert slot_status(25, True, True) == "late"

def test_slot_status_morning_open():
    assert slot_status(40, True, False) == "open"

def test_slot_status_evening_late():
    assert slot_status(5, False, False) == "late"

def test_slot_status_missed():
    assert slot_status(-10, False, False) == "missed"
