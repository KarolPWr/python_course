import pytest
from decoder_exercise_solution import Decoder

@pytest.fixture
def user():
    yield "User12"

@pytest.fixture
def decoder():
    yield Decoder()

"""
before yield we have setup-like code 
then after yield we can execute some teardown-like code 
fixtures have benefit that thay can be easily shared for many tests
fixtures provide context for tests 
if defined here they are automatically applied to test method when pytest encounters corresponding name 
@pytest.fixture(scope=class) - equivalent to setUpClass, tearDownClass 
pytest also has parametrization fixtures
pytest also can output in defined format, xml for example 
"""
