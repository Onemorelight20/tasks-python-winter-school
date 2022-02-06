import enum


class Category(enum.Enum):
    PLUMBING = 0
    WOODEN_PRODUCT = 1
    PAINT = 2
    FURNITURE = 3

class PhysicalProperties:
    # weight in kilograms & size measurement in meters
    def __init__(self, weight: float, height: float, width: float, length: float) -> None:
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length

    def get_packing_volume_in_cubic_meters(self) -> float:
        return self.height * self.width * self.length

class Item:
    def __init__(self, name: str, category: Category, price: float, physical_properties: PhysicalProperties) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.physical_properties = physical_properties

class Sink(Item):
    def __init__(self, name: str, category: Category, price: float, physical_properties: PhysicalProperties, color: str, material: str) -> None:
        super().__init__(name, category, price, physical_properties)
        self.color = color
        self.material = material

class Door(Item):
    def __init__(self, name: str, category: Category, price: float, physical_properties: PhysicalProperties, type_of_wood:str, has_glass: bool) -> None:
        super().__init__(name, category, price, physical_properties)
        self.type_of_wood = type_of_wood
        self.has_glass = has_glass

class BlackPaint(Item):
    def __init__(self, name: str, category: Category, price: float, physical_properties: PhysicalProperties, type_of_paint: str, max_area: float) -> None:
        super().__init__(name, category, price, physical_properties)
        self.type_of_paint = type_of_paint
        self.max_area = max_area


class Hypermarket:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def pop_item(self, item: Item) -> Item:
        if item in self.items:
            idx = self.items.index(item)
            return self.items.pop(idx)
        else:
            return None


class ItemManager:
    def __init__(self, hypermarket: Hypermarket) -> None:
        self.hypermarket = hypermarket

    def find_by_categories(self, *categories: Category) -> list[Item]:
        result = []
        for item in self.hypermarket.items:
            if item.category in categories:
                result.append(item)
        return result


    def find_by_price_and_category(self, category: Category, price: float) -> list[Item]:
        result = []
        for item in self.hypermarket.items:
            if item.category == category and item.price <= price:
                result.append(item)
        return result

    def get_sorted_by_weight(items: list[Item], asc: bool = True) -> list[Item]:
        return sorted(items, key = lambda x: x.physical_properties.weight, reverse=asc)

    def get_sorted_by_price(items: list[Item], asc: bool = True)  -> list[Item]:
        return sorted(items, key = lambda x: x.price, reverse=asc)

print('success!')
