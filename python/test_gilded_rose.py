# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    def test_update_qualityBasedOnRule(self):

        original_quality = 25
        original_sell_in = 24
        items = [Item("OBJ", original_sell_in, original_quality)]
        gilded_rose = GildedRose(items)

        # Check for original data
        self.assertEqual(original_quality, items[0].quality)

        # Check for bottom edge case
        qualityUpdated_case_edgeDw = 0
        gilded_rose.update_qualityBasedOnRule (items[0], qualityUpdated_case_edgeDw)
        self.assertEqual(qualityUpdated_case_edgeDw, items[0].quality)
        qualityUpdated_case_edgeDw = -1
        gilded_rose.update_qualityBasedOnRule (items[0], qualityUpdated_case_edgeDw)
        self.assertNotEqual(qualityUpdated_case_edgeDw, items[0].quality)

        # Cehck for normal case
        qualityUpdated_case_normal = 12
        gilded_rose.update_qualityBasedOnRule (items[0], qualityUpdated_case_normal)
        self.assertEqual(qualityUpdated_case_normal, items[0].quality)

        # Cehck for upper edge cases
        qualityUpdated_case_edgeUp = 50
        gilded_rose.update_qualityBasedOnRule (items[0], qualityUpdated_case_edgeUp)
        self.assertEqual(qualityUpdated_case_edgeUp, items[0].quality)
        qualityUpdated_case_edgeUp = 51
        gilded_rose.update_qualityBasedOnRule (items[0], qualityUpdated_case_edgeUp)
        self.assertNotEqual(qualityUpdated_case_edgeUp, items[0].quality)

        return

    # def testcheck_isSellInInRange(self):
    #     return item_obj.sell_in >= 0

    # # Check if Conjured
    # def check_isConjured(self, item_obj):
    #     return "Conjured" in item_obj.name


if __name__ == '__main__':
    unittest.main()
