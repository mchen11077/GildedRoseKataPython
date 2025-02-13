# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
class Updater:
    # Base Case
    def update(self, item: Item):
        pass

class DefaultUpdater(Updater):
    def update(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

class SulfurasUpdater(Updater):
    def update(self, item: Item):
        pass

class AgedBrieUpdater(Updater):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

class BackstagePassUpdater(Updater):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = self.get_updater(item)
            updater.update(item)
    
    def get_item(self):
        return [item.name for item in self.items]
    
    def add_item(self, name, sell_in, quality):
        self.items.append(Item(name, sell_in, quality))
    
    def get_updater(self, item: Item) -> Updater:
        if item.name == "Sulfuras":
            return SulfurasUpdater()
        elif item.name == "Aged Brie":
            return AgedBrieUpdater()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        else:
            return DefaultUpdater()
