from database.DB_connect import DBConnect

class SaleDAO:
    @staticmethod
    def getAllAnni()-> set[tuple[int]] | None:
        cnx = DBConnect.get_connection()
        result = set()
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query = """SELECT year(gds.`Date`) 
                     FROM go_daily_sales gds"""
            cursor.execute(query)
            result = set(cursor.fetchall())
            cursor.close()
            cnx.close()
            return result

if __name__ == "__main__":
    print(SaleDAO.getAllAnni())