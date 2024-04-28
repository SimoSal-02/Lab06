import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer_code = None

    def fillYears(self):
        years = self._model.getAllAnni()
        for year in years:
            self._view.dd_anno.options.append(ft.dropdown.Option(year[0]))
        self._view.update_page()

    def fillBrands(self):
        for brand in self._model.getAllBrands():
            self._view.dd_brand.options.append(ft.dropdown.Option(brand))
        self._view.update_page()

    def fillRetailers(self):
        for retailer in self._model.getAllRetailers():
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.retailer_code,
                                                                     text=retailer.retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self,e):
        if e.control.data is None:
            self._retailer_code = None
        else:
            self._retailer_code = e.control.data.retailer_code



    def handleAnalizzaVendite(self,e):
        self._view.txt_result.controls.clear()
        t = self._model.getAnalisiVendite(self._anno,self._brand, self._retailer_code)
        self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite:\nGiro d'affari: {t[0][0]}\nNumero di vendite. {t[0][1]}\nNumero retailers coinvolti: {t[0][2]}\nNumero prodotti: {t[0][3]}"))
        self._view.update_page()

    def getTopVendite(self,e):
        self._view.txt_result.controls.clear()
        for vendite in self._model.getTopVendite(self._anno,self._brand, self._retailer_code):
            self._view.txt_result.controls.append(ft.Text(f"Data: {vendite[0]}; Ricavo: {vendite[1]}; Retailer: {vendite[2]}; Product: {vendite[3]};"))
        self._view.update_page()
    def leggi_anno(self,e):
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value

    def leggi_brand(self,e):
        if e.control.value == "None":
            self._brand = None
        else:
            self._brand = e.control.value


