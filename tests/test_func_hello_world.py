from app.function import func_hello_world

def test_func_hello_world():
    output = func_hello_world()
    expected = "Hello World!"
    assert output == expected