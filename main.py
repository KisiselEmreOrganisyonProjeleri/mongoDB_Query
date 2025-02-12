from employee_db import EmployeeDB
def main():
    employee_db = EmployeeDB('Employee')
    data = [{
        "firstname":'Emre',
        "lastname":'Kayis',
        "department": "Analytics",
        "qualification":'BE',
        "age":23
    },
    {
        "firstname":'Kursat',
        "lastname":'Guney',
        "department": "IT",
        "qualification":'BE',
        "age":55
    },
    {
        "firstname":'Ramazan',
        "lastname":'Kılıc',
        "department": "Insan Kaynakları",
        "qualification":'BE',
        "age":22
    },
    {
        "firstname":'Nadir',
        "lastname":'Yasar',
        "department": "Kordinasyon",
        "qualification":'BE',
        "age":36
    },
    {
        "firstname":'Ozkan',
        "lastname":'Kurukavak',
        "department": "Motivasyon Sefi",
        "qualification":'BE',
        "age":38
    }]
    employee_db.coklu_calisan_ekleme(data)
    for emp in employee_db.yasina_ve_kalitesine_gore_calisan_bulma("BE",30):
        print(emp)


if __name__ == '__main__':
    main()
