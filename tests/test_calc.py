from src.calc import reverse_string, hello
import pytest

# def test_reverse_string(number_list):
#     assert reverse_string(number_list) == 'gelo'

@pytest.mark.parametrize('x, y', [('123', '321'), ('hello', 'olleh'), ('vera', 'arev')])
def test_reverse_string(x, y):
    assert reverse_string(x) == y

def test_hello():
    assert hello('world') == 'Hello world'