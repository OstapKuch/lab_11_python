from Lab_11.Models.Animator import Animator
from Lab_11.Models.Location import Location
from Lab_11.Models.Masterclass_type import MasterclassType
from Lab_11.Models.Quest import Quest
from Lab_11.Models.TrampolineJumping import TrampolineJumping
from Lab_11.Models.AnimatorType import AnimatorType


class HolidayManager:

    def __init__(self, holiday_list):
        self.holiday_list = holiday_list

    def sort_holiday_list_by_price(self, reverse):
        return sorted(self.holiday_list, key=lambda holiday: holiday.price, reverse=reverse)

    def sort_holiday_list_by_duration(self, reverse):
        return sorted(self.holiday_list, key=lambda holiday: holiday.duration, reverse=reverse)

    def find_holiday_by_children_number(self, children_number):
        return list(filter(lambda holiday: holiday.children_number == children_number, self.holiday_list))


animator = Animator(200, 1.30, 5, 12, AnimatorType.CLOWN, 2)
quest = Quest(400, 2.5, 5, 15, Location.PARK, MasterclassType.APPLIQUE)
trampoline = TrampolineJumping(150, 1.2, 3, 8, 5)
holidays = [animator, quest, trampoline]
manager = HolidayManager(holidays)

print(manager.sort_holiday_list_by_price(False))
print(manager.sort_holiday_list_by_duration(True))
print(manager.find_holiday_by_children_number(5))
