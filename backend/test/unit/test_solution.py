import pytest
#import unittest.mock as mock
from unittest.mock import patch, MagicMock

from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet
#from src.util.calculator import calculate_readiness

# add your test case implementation here
# @pytest.mark.unit
# def test():
#     pass

items = [
    {"name": "Egg", "quantity": 100}, 
    {"name": "Milk", "quantity": 10}]

@pytest.fixture
def sut():
    mocked_dao = MagicMock()
    mocked_controller = RecipeController(mocked_dao)

    return mocked_controller

@pytest.mark.unit
def test_get_avaiable_items_1(sut):
    with patch.object(RecipeController, 'get_all') as mock_get_all:
        mock_get_all.return_value = items
        result = sut.get_available_items(minimum_quantity=-1)
        assert result == {"Egg": 100, "Milk": 10}

@pytest.mark.unit
def test_get_avaiable_items_2(sut):
    with patch.object(RecipeController, 'get_all') as mock_get_all:
        mock_get_all.return_value = items
        result = sut.get_available_items(minimum_quantity=10)
        assert result == {"Egg": 100}

@pytest.mark.unit
def test_get_avaiable_items_3(sut):
    with patch.object(RecipeController, 'get_all') as mock_get_all:
        mock_get_all.return_value = items
        result = sut.get_available_items(minimum_quantity=100)
        assert result == {}
