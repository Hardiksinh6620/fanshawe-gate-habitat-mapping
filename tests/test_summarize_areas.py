import unittest
from examples.summarize_areas import summarize

class AreaTests(unittest.TestCase):
    def setUp(self):self.rows=[dict(id='a',habitat='grass',area_m2=100),dict(id='b',habitat='wood',area_m2=300)]
    def test_known_totals(self):
        r=summarize(self.rows)
        self.assertEqual(r['total_area_m2'],400)
        self.assertEqual([v['percent_of_supplied_area'] for v in r['categories']],[25,75])
        self.assertFalse(r['geometry_validated'])
    def test_duplicate_identifier_rejected(self):
        with self.assertRaises(ValueError):summarize([self.rows[0],self.rows[0]])
    def test_empty_rejected(self):
        with self.assertRaises(ValueError):summarize([])
    def test_invalid_area_rejected(self):
        for area in [0,-1,True,float('nan'),float('inf')]:
            with self.subTest(area=area),self.assertRaises(ValueError):summarize([{**self.rows[0],'area_m2':area}])
    def test_order_independence(self):self.assertEqual(summarize(self.rows),summarize(reversed(self.rows)))
    def test_same_category_is_aggregated(self):
        rows=[self.rows[0],{**self.rows[1],'habitat':'grass'}]
        self.assertEqual(summarize(rows)['categories'][0]['area_m2'],400)
