import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy:

    def test_dummy(self):
        print("test line 1 ")
        print("test line 2")
        self.driver.get("http://localhost/quicksite/")
