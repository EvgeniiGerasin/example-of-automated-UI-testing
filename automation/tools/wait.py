from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tools.helper import Screenshot
from tools.exceptions import BadElementException





# # *********************************************************
class WaitElement:
    """Содержит методы для ожидания элементов страницы
    """
    @staticmethod
    def xpath(driver, locator, timeout) -> None:
        """Waiting for the xpath element
        to appear on the page

        Args:
        - driver (object): instance webdriver
        - locator (str): xpath
        - timeout (int): time to wait for the element
        (default 10 sec)
        """
        if timeout == None:
            timeout = 10
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        except:
            Screenshot().shot(driver, f'Wait error: {locator}')
            text_exception = f'Wait element: {locator}'
            raise BadElementException(text_exception)

# class CastomWait:

#     CONDITION = True

#     def __init__(self) -> None:
#         self.condition = True


#     def run(self, timeout=None) -> None:
#         pass

# # b = CastomWait()
# # print(b.condition)
# # b.condition = False
# # print(b.condition)
# # print(b.condition)
# # b.run(5)
# # class A:

# #     def __init__(self, f) -> None:
# #         self.f = f

# #     def func(self):
# #         self.f

# # a = A(b.run(5))
# # a.func()


class CastomWait:

    def __init__(self) -> None:
        self.loading_bar = True
        self.loading_list = True
        self.loading_block = True

    def run(self):
        pass
        # print(self.loading_bar)
        # print(self.loading_list)
        # print(self.loading_block)


class MyClass:

    def __init__(self, wait_class) -> None:
        self.wait = wait_class

    def test(self, **kwarg):
        # if 
        # print(self.wait.loading_bar)
        # print(self.wait.loading_list)
        # print(self.wait.loading_block)
        # print("-------------")
        # self.wait.run()
        pass


# waint_1 = CastomWait()
# action = MyClass(waint_1)
# action.test()
# print()
# action.wait.loading_bar = False
# action.test()
# print()
# action.wait.loading_bar = True
# action.test()
