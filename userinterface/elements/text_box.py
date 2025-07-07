from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto_core.elements.constants.element_state import ElementState
from py_selenium_auto_core.locator.locator import Locator


class CustomTextBox(TextBox):
    def __init__(self, locator: Locator, name: str, element_state: ElementState):
        super().__init__(locator, name, element_state)

    @property
    def text(self) -> str:
        return self.value
