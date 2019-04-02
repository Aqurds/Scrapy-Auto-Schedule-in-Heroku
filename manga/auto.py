import os
import time
import schedule as sc
import pymongo
import json

# making connection with mLab for updating the document
connection = pymongo.MongoClient("ds159785-a0.mlab.com", 59785)
db = connection["mangastuff"]
db.authenticate("user", "2252010baby")


# function for running all spiders
def update():
    os.system('scrapy crawl manganame')
    time.sleep(120)
    os.system('scrapy crawl manga_details')
    time.sleep(120)
    os.system('scrapy crawl manga_chapter_list')
    time.sleep(120)
    os.system('scrapy crawl update_spider')
    time.sleep(120)
    os.system('scrapy crawl manga_each_chapter_image_list_with_manga_id')



# function for deleting old document and keeping the new document
def update_document():
    updatable_manga_id = []
    old_chapter_number = 0

    # get the updatable manga id from database
    manga_link = db['manga_name_updater_list'].find()

    if manga_link:
        for item in manga_link:
            for url in item['individual_manga_url']:
                updatable_manga_id.append(url.split('/')[-1])



    for item in updatable_manga_id:
        # delete old document from all_manga_details code
        all_manga_details_result = list(db['all_manga_details'].find({'id': item}))
        if len(all_manga_details_result) > 1:
            db['all_manga_details'].remove({'_id': all_manga_details_result[0]['_id']})
            # print("first duplicate record deleted. id: ", all_manga_details_result[0]['_id'])

        # delete old document from manga_chapter_list code
        manga_chapter_list_result = list(db['manga_chapter_list'].find({'manga_id': item}))
        if len(manga_chapter_list_result) > 1:
            old_chapter_number = len(manga_chapter_list_result[0]['chapter_id'])
            db['manga_chapter_list'].remove({'_id': manga_chapter_list_result[0]['_id']})
            # print(old_chapter_number)

        # delete old document from manga_each_chapter_image_list_with_manga_id code
        manga_each_chapter_image_list_with_manga_id_result = list(db['manga_each_chapter_image_list_with_manga_id'].find({'manga_id': item}))
        if len(manga_each_chapter_image_list_with_manga_id_result) > old_chapter_number:
            for x in range(0, old_chapter_number):
                db['manga_each_chapter_image_list_with_manga_id'].remove({'_id': manga_each_chapter_image_list_with_manga_id_result[x]['_id']})


# function for deleting old documents from the collection so the spiders will always work with new updated content
def delete_previous_document():
    connection = pymongo.MongoClient("ds159785-a0.mlab.com", 59785)
    db = connection["mangastuff"]
    db.authenticate("user", "2252010baby")
    db['manga_name_updater_list'].remove({})
    db['manga_chapter_updater_list'].remove({})


# running all the function with schedule each day
sc.every().day.at("00:20").do(update)
sc.every().day.at("01:00").do(update_document)
sc.every().day.at("01:30").do(delete_previous_document)



while 1:
    sc.run_pending()
    time.sleep(1)
