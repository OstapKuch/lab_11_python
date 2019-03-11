from Lab_11.Models.HolidayForChildren import HolidayForChildren


class Quest(HolidayForChildren):
    def __init__(self, price, duration, children_number, age_category, location, difficulty):
        super().__init__(price, duration, children_number, age_category)
        self.location = location
        self.difficulty = difficulty
