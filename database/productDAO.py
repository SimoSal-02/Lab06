from database.DB_connect import DBConnect

class ProductDAO:
    @staticmethod
    def getAllBrands() -> list[str] | None:
        cnx = DBConnect.get_connection()
        result=[]
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query = """select distinct (gp.Product_brand) 
                    from go_products gp """
            cursor.execute(query)
            result =[brand[0] for brand in cursor.fetchall()]
            cursor.close()
            cnx.close()
            return result

