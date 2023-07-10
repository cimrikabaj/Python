#1
# a = {
#     "fullname": "Ram",
#     "contact": "9840504313",
#     "school": [
#         {"name": "ABC School", "year": "2020"},
#         {"name": "XYZ College", "year": "2023"},
#     ],
#     "address":[
#         {"city": "Ktm", "from": "2010", "to": "2015"},
#         {"city": "Lalitpur", "from": "2017", "to": "2023"},
#     ]
# }

#######Profile########
# Full Name: Ram
# Contact:9840504313
# School 1:ABC College, Year:2020
# School 2:XYZ College, Year:2023
# Address 1:ktm(2010 to 2015)
# Address 1:ktm(2017 to 2023)

# print("#####profile#######")
# print(f"Full Name: {a.get('fullname')}") 
# print(f"Contact:{a.get('contact')}")
# schools=a.get("school")
# for idx,school in enumerate(schools,1):
#     print(f"school {idx}:{school.get('name')}, year:{school.get('year')}")

#2.
# a=["AC5456","AD5789","AE7332","ZZ6009","VB1765"]

# for i in a:
#     b.append(i[3:])
# print(b)


#solution
#print(sum(map(lambda n:int(n[3:],a),a)))
#or
#total=0
# for i in a:
#     total=total+int(i[3:])
# print(total)

#3.
#from 1 to 50 print "go" if divisible by 3 
#print "done" id divisible by 5
#print"done and go" if divisible by both
#print "none" if not divisible by any
# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("done and go")
#     elif i % 3 == 0:
#         print("go")
#     elif i % 5 == 0:
#         print("done")
#     else:
#         print("none")

#4.
#find the sum of multiples of 3,5 and 15 between 1 to 100
# total=0
# for i in range(1,10):
#     if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
#         total+=i
# print(total)

#or
#print(sum(filter(lambda n :n % 3 == 0 or n % 5 ==0 or n % 15 == 0, range(1,101))))


#5.
# a=["python",78,"hello",12,10,6,8,"apple",60]
# #total=78+98+12+10+6+8+54+60
# total=0
# for i in a:
#     if isinstance(i,int):
#         total+=i
# print(total)
#or
#print(sum(filter(lambda n : isinstance(n,int),a)))

# a=["python",78,"98","hello",12,10,6,8,"apple","9",60]
# print(sum(map(int,filter(lambda n : isinstance(n,int)or(isinstance(n,str)and n.isnumeric()),a))))

# total=0
# for i in a:
#     if isinstance(i,str) and i.isnumeric():
#         total+=int(i)
#     else:
#         total+=i
# print(total)

#day 19

#1.
results = [
    {
        "name": "Ram",
        "address": "Ktm",
        "reg_number": 216712,
        "marks_obtained":[
            {"subject": "Maths", "score": 80},
            {"subject": "Computer", "score": 90},
        ]
    },
    {
        "name": "Sita",
        "address": "Ktm",
        "reg_number": 278322,
        "marks_obtained":[
            {"subject": "Maths", "score": 85},
            {"subject": "Computer", "score": 95},
        ]
    },
    {
        "name": "Hari",
        "address": "Bkt",
        "reg_number": 329876,
        "marks_obtained":[
            {"subject": "Maths", "score": 88},
            {"subject": "Computer", "score": 89}
        ]
    },
]

########### Result ###########
# Name: Ram
# Address: Ktm
# Registration Number: 216712
# Marks obtained in Maths: 
# Marks obtained in Computer:
# Total Marks:
# Percentage:

for i in results:
    print(f"Name: {i['name']}")
    print(f"Address: {i['address']}")
    print(f'Registration Number: {i["reg_number"]}')
    print(f'Marks obtained in Maths: {i["marks_obtained"][0]["marks"]}')
    print(f'Marks obtained in Science: {i["marks_obtained"][1]["marks"]}')
    print(f'Total Marks: {i["marks_obtained"][0]["marks"] + i["marks_obtained"][1]["marks"]}')
    print(f'Percentage: {(i["marks_obtained"][0]["marks"] + i["marks_obtained"][1]["marks"])/2}')
    print('------------------------------------')

#2.
a = [
    {"name": "Ram", "score": 85},
    {"name": "Hari", "score": 90},
    {"name": "Sita", "score": 96},
    {"name": "Suraj", "score": 89},
    {"name": "Gita", "score": 88},
]

# sort in descending order the above given list on the basis of score