from database.DB_connect import DBConnect
from model.retailer import Retailer

class RetailerDAO:
    @staticmethod
    def getAllRetailers(map)->list[Retailer] | None:
        cnx = DBConnect.get_connection()
        result=[]
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query = """SELECT gr.*
                    FROM go_retailers gr"""
            cursor.execute(query)
            for retailer in cursor.fetchall():
                ret = Retailer(retailer[0],retailer[1],retailer[2],retailer[3])
                result.append(ret)
                map[retailer[0]]=ret
            cursor.close()
            cnx.close()
            return result
    @staticmethod
    def getTopVendite(anno,brand,retailer) -> list[tuple] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("errore connessione")
            return None
        else:
            cursor = cnx.cursor()
            query = """select gds.`Date` ,(gds.Unit_sale_price*gds.Quantity), gds.Retailer_code,gds.Product_number 
                     from go_daily_sales gds, go_products gp 
                     where gds.Product_number=gp.Product_number and year(`Date`)=coalesce(%s ,year (`Date`)) and gp.Product_brand = coalesce (%s ,gp.Product_brand) and Retailer_code=coalesce(%s ,Retailer_code)
                     order by (gds.Quantity*gds.Unit_sale_price) desc 
                     limit 5"""
            cursor.execute(query,(anno,brand,retailer))
            results = cursor.fetchall()
            cursor.close()
            cnx.close()
            return results
    @staticmethod
    def getAnalisiVendite(anno,brand,retailer) -> tuple | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("errore connessione")
            return None
        else:
            cursor = cnx.cursor()
            query = """select sum((gds.Unit_sale_price*gds.Quantity)),count(gp.Product_number),count(distinct (gds.Retailer_code)),count(distinct (gds.Product_number))
                    from go_daily_sales gds, go_products gp 
                    where gds.Product_number=gp.Product_number 
                    and year(`Date`)=coalesce(%s ,year (`Date`)) 
                    and gp.Product_brand = coalesce (%s  ,gp.Product_brand) 
                    and gds.Retailer_code=coalesce(%s ,gds.Retailer_code)  """
            cursor.execute(query,(anno,brand,retailer))
            results = cursor.fetchall()
            cursor.close()
            cnx.close()
            return results


if __name__ == "__main__":
    print(RetailerDAO.getAllRetailers())
