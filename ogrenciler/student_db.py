from mongodb_connect import MongoDBConnection

class StudentDB(MongoDBConnection):
    def __init__(self,db_name):
        super().__init__()
        self.collection = self.database_getir(db_name)["ogrenciSkorları"]
    
    def ogrenci_skorlarını_ekleme(self,data:dict):
        self.collection.insert_many(data)
    
    def toplam_ders_sorgulama(self):
        return self.collection.aggregate([
            {
                "$group":{
                    "_id":'$user',
                    "Toplam Dersler": {'$sum':1}
                }
            }
        ])
    def toplam_puan_sorgulama(self):
        return self.collection.aggregate([
            {
                "$group":{
                    "_id":'$user',
                    "Toplam Skorlar": {'$sum':"$score"}
                }
            }
        ])
    def ogrenci_ortalama_puan_hesaplama(self):
        return self.collection.aggregate([
            {"$group":{
                '_id':'$user',
                "Ortalama Puanlar": {'$avg':'$score'}
            }
             }
        ])