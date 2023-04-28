# -*- coding: utf-8 -*-

class GildedRose(object):

    QUALITY_RANGE_UPPER = 50
    QUALITY_RANGE_LOWER = 0

    def __init__(self, items):
        self.items = items

    # Will the item quality degrade as time
    # surpass the sell_in time
    def check_Item_isDegradable(self, item_obj):
        is_brie  = item_obj.name == "Aged Brie"
        is_hand  = item_obj.name == "Sulfuras, Hand of Ragnaros"
        is_pass  = item_obj.name == "Backstage passes to a TAFKAL80ETC concert"
        return (not (is_brie or is_hand or is_pass))

    # Update quality based on the following rules
    # - Quality range will not surpass 50
    # - QUality range will not go below 0
    def update_qualityBasedOnRule(self, item, qualityUpdated):
        is_upperBorund = (qualityUpdated >= self.QUALITY_RANGE_LOWER)
        is_lowerBorund = (qualityUpdated <= self.QUALITY_RANGE_UPPER)
        if (is_upperBorund and is_lowerBorund):
            item.quality = qualityUpdated
            return
        else:
            return

    # Check sell in in range
    # - if sell_in is above zero return true
    # - otherwise return false
    def check_isSellInInRange(self, item_obj):
        return item_obj.sell_in >= 0;

    # Check if Conjured
    def check_isConjured(self, item_obj):
        return "Conjured" in item_obj.name


    def update_quality(self):
        for item in self.items:

            # Ignore update logic on "Sulfuras, Hand of Ragnaros"
            if  (item.name=="Sulfuras, Hand of Ragnaros"):    continue

            # Item degradable
            if (self.check_Item_isDegradable(item)):
                if (self.check_isSellInInRange(item)):  self.update_qualityBasedOnRule(item, item.quality+1*(2 if self.check_isConjured(item) else 1))
                else:                                   self.update_qualityBasedOnRule(item, item.quality+2*(2 if self.check_isConjured(item) else 1))

            # Item non-degradable
            else:
                if  (item.name=="Aged Brie"):                     self.update_qualityBasedOnRule(item, item.quality+1)
                elif(item.name=="Backstage passes to a TAFKAL80ETC concert"):
                    if  (10 < item.sell_in      ):                self.update_qualityBasedOnRule(item, item.quality+1)
                    elif(5  < item.sell_in <= 10):                self.update_qualityBasedOnRule(item, item.quality+2)
                    elif(     item.sell_in <=  5):                self.update_qualityBasedOnRule(item, item.quality+3)
                    else:                                         self.update_qualityBasedOnRule(item, 0)


            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
