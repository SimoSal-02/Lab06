from database.saleDAO import SaleDAO
from database.productDAO import ProductDAO
from database.retailerDAO import RetailerDAO
class Model:
    def __init__(self):
        self._saleDAO = SaleDAO()
        self._productDAO = ProductDAO()
        self._retailerDAO = RetailerDAO()
        self._retailersMap = {}

    def getAllAnni(self):
        return self._saleDAO.getAllAnni()

    def getAllBrands(self):
        return self._productDAO.getAllBrands()

    def getAllRetailers(self):
        return self._retailerDAO.getAllRetailers(self._retailersMap)

    def getTopVendite(self,anno,brand,retailer):
        return self._retailerDAO.getTopVendite(anno,brand,retailer)

    def getAnalisiVendite(self,anno,brand,retailer):
        return self._retailerDAO.getAnalisiVendite(anno,brand,retailer)
