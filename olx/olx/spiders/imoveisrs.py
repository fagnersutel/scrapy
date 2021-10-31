import scrapy
class ImoveisrsSpider(scrapy.Spider):
    name = 'imoveisrs'
    allowed_domains = ['rs.olx.com.br']
    #start_urls = ['https://rs.olx.com.br/imoveis/comercio-e-industria']
    start_urls = ['https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/imoveis/comercio-e-industria']
    start_urls = ['https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul?q=box%20garagem']
    def parse(self, response):
        #items = response.xpath('//ul[@id="ad-list"]/li[not(contains(@class,"list_native"))]')
        #items = response.xpath('//ul[@id="ad-list"]/li[not(contains(descendant::div]')
        #items = response.xpath('//ul[@id="ad-list"]/li[not(contains(descendant::div]')
        items = response.xpath('//ul[@id="ad-list"]/li[descendant::a]')
        self.log(len(items))
        for item in items:
            #url = self.log(item.xpath('./a/@href').extract_first())
            url = item.xpath('./a/@href').extract_first()
            print("aa" + url)
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        titulo = response.xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div[14]/div/div/h1/text()').extract_first()
        #print(titulo)
        classe = response.xpath('//dt[contains(text(), "Categoria")]/following-sibling::a/text()').extract_first()
        Tamanho = response.xpath('//dt[contains(text(), "Tamanho")]/following-sibling::a/text()').extract_first()
        Condominio = response.xpath('//dt[contains(text(), "Condomínio")]/following-sibling::dd[1]/text()').extract_first()
        Municipio = response.xpath('//dt[contains(text(), "Município")]/following-sibling::dd[1]/text()').extract_first()
        Bairro = response.xpath('//dt[contains(text(), "Bairro")]/following-sibling::dd[1]/text()').extract_first()
        valor = response.xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div[12]/div/div/div/div/div[1]/div/h2/text()').extract_first()
        imagem =  response.xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div[29]/div/div/div/div[2]/div/div[1]/div[1]/img/@src').extract_first()
        urls = response

        # yield{
        #      'titulo'   : titulo,
        #      'classe'   : classe,
        #      'Tamanho'   : Tamanho,
        #      'Condominio' : Condominio,
        #      'valor'    : valor,
        # }

        if titulo:
            print("\nImóvel: " + titulo)
            if classe:
                print("Classe: " + classe)
            if Tamanho:
                print("Tamanho: " + Tamanho)
            if Condominio:
                print("Condominio: " + Condominio)
            if Municipio:
                print("Municipio: " + Municipio)
            if Bairro:
                print("CondomBairroinio: " + Bairro)
            if valor:
                print("Valor: " + valor)
            if imagem:
                print("Imagem: " + imagem)
                print("URL: " + response.request.url)
            print("\n")
