import scrapy

class EngravingItem(scrapy.Item):
    nom_gravure = scrapy.Field()
    indice = scrapy.Field()
    matiere = scrapy.Field()
    haut_de_montage = scrapy.Field()
    fournisseur = scrapy.Field()
    premiere_gravure = scrapy.Field()

