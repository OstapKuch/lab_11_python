from Lab_11.Models.HolidayForChildren import HolidayForChildren


class TrampolineJumping(HolidayForChildren):
    def __init__(self, price, duration, children_number, age_category, size):
        super().__init__(price, duration, children_number, age_category)
        self.size = size
