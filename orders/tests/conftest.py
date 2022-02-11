import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    """Фикстура для клиента API."""
    return APIClient()


@pytest.fixture
def category_factory():
    def factory(**kwargs):
        return baker.make("Category", **kwargs)
    return factory


@pytest.fixture
def shop_factory():
    def factory(**kwargs):
        return baker.make("Shop", **kwargs)
    return factory


@pytest.fixture
def contact_factory():
    def factory(**kwargs):
        return baker.make("Contact", **kwargs)
    return factory
