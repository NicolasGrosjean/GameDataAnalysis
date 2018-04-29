import scrapy

class QuotesSpider(scrapy.Spider):
    name = "parser"
    start_urls = [
        'http://steamcharts.com/app/236850',
		'http://steamcharts.com/app/203770',
		'http://steamcharts.com/app/281990',
		'http://steamcharts.com/app/394360'
    ]

    def parse(self, response):
        gameId = response.url.split("/")[-1]
        for line in response.xpath(".//tr"):
            month = line.xpath('.//td[1]/text()').re(r'[ \w]+')
            yield {
				'gameId' : gameId,
				'month': month[0] if ((month != None) & (len(month) != 0)) else None,
				'avgPlayers': line.xpath('.//td[2]/text()').extract_first(),
				'gain': line.xpath('.//td[3]/text()').extract_first(),
				'percGain': line.xpath('.//td[4]/text()').extract_first(),
				'peakPlayers': line.xpath('.//td[5]/text()').extract_first()
            }
