"""Method module

.. autosummary::

   SampleClass
   SampleClass.leepyear
   SampleClass.hello
"""


class SampleClass:
    """[summary]"""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def leepyear(year: str) -> bool:
        """[summary]

        Args:
            year (str): [description]
            year (str): [description]

        Returns:
            bool: [description]
        """
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False

    def hello(self) -> None:
        """[summary]

        Args:
            なし

        Returns:
            なし
        """
        print("Hello, " + self.name)
