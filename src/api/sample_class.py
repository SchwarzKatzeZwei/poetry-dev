"""Method module

.. autosummary::

   SampleClass
   SampleClass.leepyear
   SampleClass.hello
"""


class SampleClass:
    """サンプルクラス"""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def leepyear(year: str) -> bool:
        """閏年判定

        Args:
            year (str): 西暦

        Returns:
            bool: 閏年ならTrue
        """
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False

    def hello(self) -> None:
        """Hello, world!"""
        print("Hello, " + self.name)
