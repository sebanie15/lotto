"""
    Lotto random variable numbers generator.
    Contains Lotto class

"""

from random import randint, sample


class Lotto:
    """
    This is class to manage the lotto play
    """

    def __init__(
        self,
        number_of_numbers_drawn: int = 6,
        min_number: int = 1,
        max_number: int = 49,
    ) -> None:
        """_summary_

        Keyword Arguments:
            number_of_numbers_drawn {int} -- _description_ (default: {6})
            min_number {int} -- _description_ (default: {1})
            max_number {int} -- _description_ (default: {49})

        Raises:
            ValueError: _description_
        """
        self.__numbers = list(range(min_number, max_number + 1))
        if number_of_numbers_drawn <= 0:
            raise ValueError("The number of numbers draw must be greater than 0!")
        self.__number_of_numbers_drawn = number_of_numbers_drawn
        self.__statistics = dict()
        self.__hits = dict()

    @property
    def number_of_numbers_drawn(self) -> int:
        """_summary_

        Returns:
            int -- Returns number of numbers to draw
        """
        return self.__number_of_numbers_drawn

    @number_of_numbers_drawn.setter
    def number_of_numbers_drawn(self, n: int = 6) -> None:
        """It is setter for number of numbers drawn

        Keyword Arguments:
            n {int} -- how many numbers dp you want to draw (default: {6})

        Raises:
            ValueError: _description_
        """
        if n <= 0:
            raise ValueError("The number of numbers draw must be greater than 0!")
        self.__number_of_numbers_drawn = n

    @property
    def statistics(self) -> dict:
        """_summary_

        Returns:
            dict: A dictionary that returns sets of drawed numbers
        """
        return self.__statistics

    def draw(self) -> list:
        """method of drawing numbers, single game

        Returns:
            list: list of the numbers
        """

        result = []
        for _ in range(1, self.number_of_numbers_drawn + 1):
            index = randint(0, len(self.__numbers) - 1)
            if f'{self.__numbers[index]}' in self.__statistics:
                self.__statistics[f'{self.__numbers[index]}'] = self.__statistics[f'{self.__numbers[index]}'] + 1
            else:
                self.__statistics[f'{self.__numbers[index]}'] = 1
            result.append(self.__numbers.pop(index))
        self.reset()
        return result

    def draw_sample(self, number_of_numbers: int = 6) -> list:
        """
        method of drawing numbers using the method from the 'random.sample' library drawing numbers

        Args:
            number_of_numbers (int, optional): The number of numbers drawn. Defaults to 6.

        Returns:
            list: List of drawn numbers.
        """
        if number_of_numbers <= 0:
            raise ValueError("number_of_numbers must be greater than 0")

        return sample(self.__numbers, k=6)

    def draw_for(self, wanted_numbers: set, number_of_draws: int = 1) -> bool:
        """_summary_

        Args:
            wanted_numbers (set): the numbers you bet on in the draw
            number_of_draws (int): _description_. Defaults to 6.

        Returns:
            bool: Returns True if the set of numbers is drawn up and False if not.
        """
        if len(wanted_numbers) == 0:
            raise ValueError("You must indicate at least one number.")

        if number_of_draws <= 0:
            raise ValueError("The number of draws must be greater than 0")

        counter = 0
        for _ in range(number_of_draws):
            counter += 1
            if set(self.draw()) == wanted_numbers:
                return True

        return False

    def draw_until_win(self, wanted_numbers: set) -> int:
        """Keep drawing until you win

        Args:
            wanted_numbers (set): Yours numbers

        Returns:
            int: Number of draw attempts
        """
        counter = 0
        drawn_numbers = {}
        draw_statistics = dict()

        while drawn_numbers != wanted_numbers:
            drawn_numbers = set(self.draw())
            counter += 1
            self.__add_hits(len(drawn_numbers & wanted_numbers))
            
        # print(draw_statistics)

        return counter

    def __add_hits(self, hitted_count: int) -> None:
        if f'{hitted_count}' in self.__hits:
            self.__hits[f'{hitted_count}'] = self.__hits[f'{hitted_count}'] + 1
        else:
            self.__hits[f'{hitted_count}'] = 1

        # self.__statistics.update(draw_statistics)

    @property
    def hits(self) -> dict:
        """A method that returns the number of times sets of numbers have been hit

        Returns:
            dict: A dictionary that returns sets of hit numbers
        """
        return self.__hits
        

    def reset(self):

        self.__numbers = list(range(1, 50))


if __name__ == "__main__":
    pass
