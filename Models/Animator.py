from Lab_11.Models.HolidayForChildren import HolidayForChildren


class Animator(HolidayForChildren):
    def __init__(self, price, duration, children_number, age_category, animator_type, quantity):
        super().__init__(price, duration, children_number, age_category)
        self.animator_type = animator_type
        self.quantity = quantity

