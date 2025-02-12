from employee_db import EmployeeDB
from inventory_db import InventoryDB
from ogrenciler.student_db import StudentDB
def main():
    # employee_db = EmployeeDB('Employee')
    # data = [{
    #     "firstname":'Emre',
    #     "lastname":'Kayis',
    #     "department": "Analytics",
    #     "qualification":'BE',
    #     "age":23
    # },
    # {
    #     "firstname":'Kursat',
    #     "lastname":'Guney',
    #     "department": "IT",
    #     "qualification":'BE',
    #     "age":55
    # },
    # {
    #     "firstname":'Ramazan',
    #     "lastname":'Kılıc',
    #     "department": "Insan Kaynakları",
    #     "qualification":'BE',
    #     "age":22
    # },
    # {
    #     "firstname":'Nadir',
    #     "lastname":'Yasar',
    #     "department": "Kordinasyon",
    #     "qualification":'BE',
    #     "age":36
    # },
    # {
    #     "firstname":'Ozkan',
    #     "lastname":'Kurukavak',
    #     "department": "Motivasyon Sefi",
    #     "qualification":'BE',
    #     "age":38
    # }]
    # employee_db.coklu_calisan_ekleme(data)
    # for emp in employee_db.yasina_ve_kalitesine_gore_calisan_bulma("BE",50):
    #     print(emp)


    #--------------------------------------------------------------------------------------------------
    # INVENTORY DB
    # inventory_db = InventoryDB('Employee')
    # inventory_data = [
    #         {"item": "canvas", "qty": 100, "size": {"h": 28, "w": 35.5, "uom": "cm"}, "status": "A"},
    #         {"item": "journal", "qty": 25, "size": {"h": 14, "w": 21, "uom": "cm"}, "status": "A"},
    #         {"item": "mat", "qty": 85, "size": {"h": 27.9, "w": 35.5, "uom": "cm"}, "status": "A"},
    #         {"item": "mousepad", "qty": 25, "size": {"h": 19, "w": 22.85, "uom": "cm"}, "status": "P"},
    #         {"item": "notebook", "qty": 50, "size": {"h": 8.5, "w": 11, "uom": "in"}, "status": "P"},
    #         {"item": "paper", "qty": 100, "size": {"h": 8.5, "w": 11, "uom": "in"}, "status": "D"},
    #         {"item": "planner", "qty": 75, "size": {"h": 22.85, "w": 30, "uom": "cm"}, "status": "D"},
    #         {"item": "postcard", "qty": 45, "size": {"h": 10, "w": 15.25, "uom": "cm"}, "status": "A"},
    #         {"item": "sketchbook", "qty": 80, "size": {"h": 14, "w": 21, "uom": "cm"}, "status": "A"},
    #         {"item": "sketch pad", "qty": 95, "size": {"h": 22.85, "w": 30.5, "uom": "cm"}, "status": "A"}
    #     ]

    #inventory_db.insert_inventory_data(inventory_data)
    #inventory_db.update_inventory_data('sketch pad', {'size.uom':'m', "status":'P'})
    #inventory_db.update_inventory_bulk({"qty":{"$lt":50}},{"size.uom":"inch","status":"P"})

    #------------------------------------------------------------------------
    # Okul Database
    students_db = StudentDB('Students')
    students_data = [
        {"user":'Emre','subject':'Database','score':80},
        {"user":'Zeynep','subject':'JavaScript','score':90},
        {"user":'Zeynep','subject':'Database','score':85},
        {"user":'Emre','subject':'JavaScript','score':75},
        {"user":'Zeynep','subject':'Data Science','score':60},
        {"user":'Emre','subject':'Data Science','score':95},
    ]
    students_db.ogrenci_skorlarını_ekleme(students_data)
    for dersler in students_db.toplam_ders_sorgulama():
        print(dersler)
    for toplam_puanlar in students_db.toplam_puan_sorgulama():
        print(toplam_puanlar)
    for ortalama_puanlar in students_db.ogrenci_ortalama_puan_hesaplama():
        print(ortalama_puanlar)
if __name__ == '__main__':
    main()
