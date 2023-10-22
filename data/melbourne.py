import math
import pandas

melbourne_data = pandas.read_csv('data/melb_data.csv')

class Col:
    SUBURB = 'Suburb'
    ADDRESS = 'Address'
    ROOMS = 'Rooms'
    TYPE = 'Type'
    PRICE = 'Price'
    METHOD = 'Method'
    SELLER_G = 'SellerG'
    DATE = 'Date'
    DISTANCE = 'Distance'
    POSTCODE = 'Postcode'
    BEDROOM2 = 'Bedroom2'
    BATHROOM = 'Bathroom'
    CAR = 'Car'
    LANDSIZE = 'Landsize'
    BUILDING_AREA = 'BuildingArea'
    YEAR_BUILT = 'YearBuilt'
    COUNCIL_AREA = 'CouncilArea'
    LATTITUDE = 'Lattitude'
    LONGITUDE = 'Longtitude'
    REGIONNAME = 'Regionname'
    PROPERTY_COUNT = 'Propertycount'


Cols = Col()


# 1400000.35218 ==> 1 400 000,35
def format_mae_price(price: float):
    return '{:,.2f}'.format(price).replace(',', ' ').replace('.', ',') + '$'