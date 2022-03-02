import os
import scrapy
import logging
from urllib.request import urlretrieve

class MangaSpider(scrapy.Spider):
    name = 'manga'
    allowed_domains = ['demon-slayer.online', 'cdn.readkakegurui.com']
    start_urls = ['http://demon-slayer.online/']

    def parse(self, response):
        manga_urls = response.xpath('//figure/ul[contains(@class, "su-posts-list-loop")]/li/a/@href').extract()[::-1]
        chapter_names = response.xpath('//figure/ul[contains(@class, "su-posts-list-loop")]/li/a/text()').extract()[::-1]
        for i, item in enumerate(zip(manga_urls, chapter_names)):
            url, chapter = item
            yield scrapy.Request(url, callback=self.parse_manga, meta={'issue_num': i, 'chapter': chapter})

    def parse_manga(self, response):
        issue_name = response.url.split('/')[-2]
        image_urls = response.xpath('//div[@class="entry-content"]/div[@class="separator"]/a/img/@src').extract()
        for url in image_urls:

            folder_dir = os.path.join('manga', issue_name)
            if not os.path.exists(folder_dir):
                os.makedirs(folder_dir)

            fp = os.path.join(folder_dir, url.rsplit('/', 1)[-1])
            yield {
                'issue_name': issue_name,
                'chapter': f'{response.meta["issue_num"]} - {response.meta["chapter"]}',
                'fp': fp,
                'url': url
            }
