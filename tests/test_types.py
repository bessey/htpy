from collections.abc import Generator
from typing import assert_type

from htpy import Element, div, li, ul


def test_element_type() -> None:
    assert_type(div, Element)
    assert_type(div(), Element)
    assert_type(div()["a"], Element)


class Test_Children:
    def test_children_as_element(self) -> None:
        child: Element = li
        ul[child]

    def test_children_as_list_element(self) -> None:
        child: list[Element] = [div]
        div[child]

    def test_children_as_generator_element(self) -> None:
        def gen() -> Generator[Element, None, None]:
            yield div

        div[gen()]
