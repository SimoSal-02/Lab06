import datetime
from dataclasses import dataclass

from model.product import Product
from model.retailer import Retailer

@dataclass
class Sale:
    date: datetime.date
    quantity: int
    unit_price: float
    unit_sale_price: float

    #relazioni
    retailer_code: int
    product_number: int
    order_method_code: int
    retailer: Retailer = None
    product: Product = None