from datetime import datetime

class FishInfo:
    def __init__(self, name: str, price_in_uah_per_kilo: float, due_date: datetime, catch_date: datetime) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.due_date = due_date
        self.catch_date = catch_date

    def set_origin(self, origin: str):
        self.origin = origin

    
class Fish(FishInfo):
    def __init__(self, name: str, price_in_uah_per_kilo: float, due_date: datetime, catch_date: datetime, age_in_months: int, weight: float) -> None:
        super().__init__(name, price_in_uah_per_kilo, due_date, catch_date)
        self.age_in_months = age_in_months
        self.weight = weight

class FishBox:
    def __init__(self, fish_info: FishInfo, summary_weight: float, package_date: datetime, height: float, length: float, width: float, is_alive: bool) -> None:
        self.fish_info = fish_info
        self.summary_weight = summary_weight
        self.package_date = package_date
        self.height = height
        self.length = length
        self.width = width
        self.is_alive = is_alive

class FishShop:
    def __init__(self) -> None:
        self.fish_boxes = {}
        self.fresh_fish = {}


    def add_fish(self, fish_box: FishBox):
        key = fish_box.fish_info.name
        if key in self.fresh_fish:
            self.fresh_fish[key].append(fish_box)
        else:
            self.fresh_fish[key] = [fish_box]

    def add_fish(self, fish: Fish):
        if fish.name in self.fresh_fish:
            self.fresh_fish[fish.name].append(fish)
        else:
            self.fresh_fish[fish.name] = [fish]


    def sell_fish(self, name:str, weight: float, is_fresh: bool):
        fish_database = None
        if is_fresh:
            fish_database = self.fresh_fish
        else:
            fish_database = self.fish_boxes

        if name in fish_database:
            list_of_fish = fish_database[name]
            return_fish = None
            for item in list_of_fish:
                if item.weight - 100 < weight < item.weight + 100:
                    return_fish = item
            if return_fish != None:
                fish_database[name].remove(return_fish)
                return return_fish
        else:
            return None        

    def get_frozen_fish_names_sorted_by_price(self):
        names = list(self.fish_boxes.keys())
        result = []
        for name in names:
            fish_boxes_with_name = self.fish_boxes[name]
            summary_price = 0
            for fish_box in fish_boxes_with_name:
                summary_price += fish_box.fish_info.price_in_uah_per_kilo

            avg_price = summary_price / len(fish_boxes_with_name)
            result.append(tuple((name, avg_price)))
        return sorted(result, key=lambda tup: tup[1])

    def get_fresh_fish_names_sorted_by_price(self):
        names = list(self.fresh_fish.keys())
        result = []
        for name in names:
            fishes_with_name = self.fresh_fish[name]
            summary_price = 0
            for fish in fishes_with_name:
                summary_price += fish.price_in_uah_per_kilo

            avg_price = summary_price / len(fishes_with_name)
            result.append(tuple((name, avg_price)))
        return sorted(result, key=lambda tup: tup[1])


print('success!')
