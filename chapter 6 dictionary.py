#dictionary

friend = {"first_name":"Patel",
          "last_name":"Sarah",
          "age":32,
          "city":"Seattle"
          }
print(friend["age"])
print(friend["city"])
print(friend["first_name"])
print(friend["last_name"])

favoutite_number = {"Garcia, Miguel":27,
                    "Smith, Emily":35,
                    "Kim, Ji-hyun":40,
                    "Dubois, Antoine":22,
                    "Johnson, Jamal":45
                    }
print(favoutite_number)

biggest_river = {"Amazon River":"Brazil",
                 "Nile River":"Egypt",
                 "Yangtze River":"China"
                 }
for name, country in biggest_river.items():
    print(name.title() + " go through "+ country)
    print(name.title())
    print(country.title())

people_1 = {"first_name":"Patel",
          "last_name":"Sarah",
          "age":32,
          "city":"Seattle"
          }

people_2 = {"first_name":"Rodriguez",
          "last_name":"Javier",
          "age":29,
          "city":"Madrid"
          }

people_3 = {"first_name":"Nguyen",
          "last_name":"Linh",
          "age":42,
          "city":"Ho Chi Minh City"
          }

peoples = [people_1,people_2,people_3]
for people in peoples:
    print(people)

cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "37 million",
        "fact": "Japan's political, economic, and cultural center"
    },
    "Istanbul": {
        "country": "Turkey",
        "population": "15 million",
        "fact": "served as the capital of the Roman, Byzantine, and Ottoman Empires"
    },
    "São Paulo": {
        "country": "Brazil",
        "population": "21 million",
        "fact": "major financial center and boasts a diverse cultural scene"
    }
}

