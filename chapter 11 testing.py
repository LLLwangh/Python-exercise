#chapter 11 testing

import unittest
from test_country_name import get_city_country


class NameTestCase(unittest.TestCase):
    def test_city_country(self):
        format_name = get_city_country('New York','US')
        self.assertEqual(format_name, 'New York, US')

unittest.main()


from survey import AnonymousSurvey
class TestAnonymousSurvey()

def city_country(city, country):
    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' - population ' + str(population)
    return output_string

