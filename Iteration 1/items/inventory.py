class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity: int) -> None:
        found = False
        for item in self.items.keys():
            if item.name == item.name:
                self.items[item].amount += quantity
                found = True
                break
        if not found:
            self.items[item] = quantity

    def remove_item(self, item_name: str, quantity: int) -> None:
        for item in self.items.keys():
            if item.name == item_name:
                self.items[item] -= quantity
                if self.items[item] <= 0:
                    self.items.pop(item)
                    break