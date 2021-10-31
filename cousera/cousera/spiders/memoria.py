scrapy shell https://www.udacity.com/courses/all
scrapy shell https://www.udacity.com/courses/all


divs = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div")
len(divs)


  scrapy shell https://www.udacity.com/courses/all
divs = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div")
aa = response.xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[2]")
print(aa)
aa.extract()
aa = response.xpath("/html/body/div[1]/div/div/div[2]/div[2]")
aa.extract()
aa = response.xpath('//*[class="card_container__25DrK"]')
aa.extract()
response.xpath("/html/body").extract()

aa = response.xpath("/html/body/div[1]/div/div/div[2]/div")
for i in aa:
    print(i)

scrapy shell https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/imoveis/comercio-e-industria

scrapy shell https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/comercio-e-industria/sala-889849086
response.xpath('//dt[contains(text(), "Tamanho")]').extract_first()

response.xpath('//dt[contains(text(), "Tamanho")]')
response.xpath('//dt[contains(text(), "Tamanho")]/following-sibling::dd[1]/text()')
response.xpath('//dt[contains(text(), "Tamanho")]/following-sibling::dd[1]/text()').extract_first()

response.xpath('//dt[contains(text(), "Condomínio")]')
response.xpath('//dt[contains(text(), "Condomínio")]/following-sibling::dd[1]/text()')
response.xpath('//dt[contains(text(), "Condomínio")]/following-sibling::dd[1]/text()').extract_first()

response.xpath('//dt[contains(text(), "Categoria")]')
response.xpath('//dt[contains(text(), "Categoria")]/following-sibling::a/text()')
response.xpath('//dt[contains(text(), "Categoria")]/following-sibling::a/text()').extract_first()

response.xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div[12]/div/div/div/div/div[1]/div/h2/text()').extract_first()

response.xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div[14]/div/div/h1/text()').extract_first()
