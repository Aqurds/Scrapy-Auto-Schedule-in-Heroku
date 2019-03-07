import os
import scrapy
import json
from ..items import MangaDetails




# This spider will use the individual manga url from the json file and will crawl each individual manga page and will collect all the details
class my_first_scrapy(scrapy.Spider):
    name = 'manga_details'

    start_urls = ["https://mangarock.herokuapp.com/manga/lovecome_like_a_demon", 
	"https://manganelo.com/manga/7_seeds", "https://mangarock.herokuapp.com/manga/dp918434", "https://mangarock.herokuapp.com/manga/ry918013", "https://mangarock.herokuapp.com/manga/fulldrum", "https://mangarock.herokuapp.com/manga/kuro_no_shoukanshi", "https://mangarock.herokuapp.com/manga/puchimasu_2", "https://mangarock.herokuapp.com/manga/uru26989466", "https://mangarock.herokuapp.com/manga/urasai", "https://manganelo.com/manga/boruto_naruto_next_generations", "https://mangarock.herokuapp.com/manga/omujo_omutsu_joshi", "https://mangarock.herokuapp.com/manga/tiger_x_crane", "https://mangarock.herokuapp.com/manga/mighty_heart", "https://mangarock.herokuapp.com/manga/ore_dake_haireru_kakushi_dungeon_kossori_kitaete_sekai_saikyou", "https://mangarock.herokuapp.com/manga/ln917521", "https://mangarock.herokuapp.com/manga/aw918496", "https://mangarock.herokuapp.com/manga/sagurichan_tankentai", "https://mangarock.herokuapp.com/manga/yuu_mii", "https://mangarock.herokuapp.com/manga/memesis", "https://manganelo.com/manga/sf917901", "https://mangarock.herokuapp.com/manga/kaiouki", "https://mangarock.herokuapp.com/manga/berserk_of_gluttony", "https://manganelo.com/manga/shokugeki_no_soma_manga", "https://mangarock.herokuapp.com/manga/legend_of_immortals",
"https://mangarock.herokuapp.com/manga/the_beast_husband", "https://mangarock.herokuapp.com/manga/tian_xing_yi_shi", "https://mangarock.herokuapp.com/manga/kindaichi_shounen_no_jikenbo_gaiden_hannintachi_no_jikenbo", "https://mangarock.herokuapp.com/manga/of917557", "https://mangarock.herokuapp.com/manga/gm918527", "https://mangarock.herokuapp.com/manga/sn918526", "https://mangarock.herokuapp.com/manga/gz918525", "https://mangarock.herokuapp.com/manga/trigun_maximum", "https://mangarock.herokuapp.com/manga/qj918524", "https://mangarock.herokuapp.com/manga/konya_wa_tsuki_ga_kirei_desu_ga_toriaezu_shi_ne", "https://mangarock.herokuapp.com/manga/kishuku_gakkou_no_juliet", "https://mangarock.herokuapp.com/manga/spirit_sword_sovereign", "https://mangarock.herokuapp.com/manga/kimi_to_ishin_denshin", "https://mangarock.herokuapp.com/manga/naze_boku_no_sekai_wo_daremo_oboeteinai_no_ka", "https://mangarock.herokuapp.com/manga/mothers_spirit", "https://mangarock.herokuapp.com/manga/all_heavenly_days", "https://mangarock.herokuapp.com/manga/zh917626", "https://mangarock.herokuapp.com/manga/vj917571", "https://mangarock.herokuapp.com/manga/castehate", "https://mangarock.herokuapp.com/manga/onideka1", "https://mangarock.herokuapp.com/manga/r402", "https://mangarock.herokuapp.com/manga/tc917676", "https://mangarock.herokuapp.com/manga/ms918512", "https://mangarock.herokuapp.com/manga/dokunie_cooking"]
    #url_dict = ''
    #json_file_name = 'manga_name.json'

    #if os.path.exists(json_file_name):
    #    with open('manga_name.json', 'r') as f:
    #        url_dict = json.load(f)

    #    for item in url_dict:
    #        for key, val in item.items():
    #            for url in val:
    #                start_urls.append(url)

    def parse(self, response):

        manga_details = MangaDetails()

        manga_details['id'] = response.url.split('/')[-1]
        manga_details['title'] = response.xpath('//div[@class="manga-info-top"]/ul/li/h1/text()')[0].extract()
        manga_details['image'] =response.xpath('//div[@class="manga-info-pic"]/img/@src')[0].extract()
        manga_details['story_alternative'] = response.xpath('//span[@class="story-alternative"]/text()').extract()
        manga_details['author'] = response.xpath('//div[@class="manga-info-top"]/ul/li[2]/a/text()').extract()
        manga_details['status'] = response.xpath('//div[@class="manga-info-top"]/ul/li[3]/text()')[0].extract().split(' : ')[-1]
        manga_details['last_updated'] = response.xpath('//div[@class="manga-info-top"]/ul/li[4]/text()')[0].extract().split(' : ')[-1]
        # manga_details['view'] = response.xpath('//div[@class="manga-info-top"]/ul/li[6]/text()')[0].extract().split(' : ')[-1]
        manga_details['genres'] = response.xpath('//div[@class="manga-info-top"]/ul/li[7]/a/text()').extract()
        manga_details['score'] = response.xpath('//em[@id="rate_row_cmd"]/em/em[2]/em/em[1]/text()')[0].extract()
        manga_details['votes'] = response.xpath('//em[@id="rate_row_cmd"]/em/em[3]/text()')[0].extract()
        manga_details['summary'] = response.xpath('//div[@id="noidungm"]/text()')[1].extract().replace("\n", "")

        yield manga_details

# Create all_manga_details.json file
