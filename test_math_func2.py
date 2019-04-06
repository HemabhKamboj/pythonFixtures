import math_func2
import pytest 

@pytest.mark.parametrize('num1 ,num2, result',   
                        [
                            (7,3,10),
                            ('Hello', 'World', 'HelloWorld'),
                            (10.5, 25.5, 36)

                        ] 
                        )
def test_add(num1, num2, result):
    assert math_func2.add(num1, num2) == result