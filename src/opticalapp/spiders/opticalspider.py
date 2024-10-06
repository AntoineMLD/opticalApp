import scrapy
from opticalapp.items import EngravingItem  # Import de l'item

class OpticalspiderSpider(scrapy.Spider):
    name = "opticalspider"
    allowed_domains = ["www.france-optique.com"]
    start_urls = ["https://www.france-optique.com/gravures"]

    def parse(self, response):
        # Extraire les liens des gravures nasales à partir de la page principale
        nasal_links = response.xpath('//div[@class="symbole_gravure"]/p/a[contains(@href, "nasale")]/@href').getall()

        for link in nasal_links:
            yield response.follow(link, callback=self.parse_nasal_engraving)

    def parse_nasal_engraving(self, response):
        item = EngravingItem()

        # Extraction du nom de la gravure
        item['nom_gravure'] = response.css('div.td.col.s3.m3 p::text').get()

        # Extraction de l'indice
        item['indice'] = response.css('div.td.col.s1.m1:nth-child(5) p::text').get()
        if item['indice']:
            item['indice'] = item['indice'].strip()
        else:
            item['indice'] = None

        # Extraction de la matière 
        item['matiere'] = response.css('div.td.col.s1.m1:nth-child(6) p::text').get()
        if item['matiere']:
            item['matiere'] = item['matiere'].strip()
        else:
            item['matiere'] = None

        # Extraction de 'haut_de_montage'
        item['haut_de_montage'] = response.xpath('//div[@class="td col s2 m2"][1]/p/text()').get()
        if not item['haut_de_montage']:
            item['haut_de_montage'] = response.css('div.td.col.s2.m2:nth-child(1) p::text').get()
        if item['haut_de_montage']:
            item['haut_de_montage'] = item['haut_de_montage'].strip()

        # Extraction du fournisseur
        item['fournisseur'] = response.xpath('//div[@class="td col s2 m2"][2]/a/span/text()').get()
        if not item['fournisseur']:
            item['fournisseur'] = response.css('div.td.col.s2.m2:nth-child(2) a span::text').get()
        if item['fournisseur']:
            item['fournisseur'] = item['fournisseur'].strip()

        # Extraction de la première gravure
        item['premiere_gravure'] = response.xpath('//div[@class="td col s1 m1"][2]/img/@src').get() or response.xpath('//div[@class="td col s1 m1"][2]/p[@class="gravure_txt"]/b/text()').get()

        yield item
