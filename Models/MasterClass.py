from Lab_11.Models.HolidayForChildren import HolidayForChildren


class MasterClass(HolidayForChildren):
    def __init__(self, price, duration, children_number, age_category, masterclass_type):
        super().__init__(price, duration, children_number, age_category)
        self.masterclass_type = masterclass_type


