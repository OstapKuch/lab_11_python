class HolidayForChildren:
    def __init__(self, price, duration, children_number, age_category):
        self.price = price
        self.duration = duration
        self.children_number = children_number
        self.age_category = age_category

    def __del__(self):
        print("Destructor called")
