import pytest_factoryboy

from . import factories

pytest_factoryboy.register(factories.CrudDemoItemFactory)
pytest_factoryboy.register(factories.ContentfulDemoItemFavoriteFactory)
