# 1) შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key'ს და ასევე შექმენით 2 ცარიელი სია for loop'ის დახმარებით პირველ სიაში დაამატეთ key ხოლო მეორე სიაში კი value ბოლოს კი გამოიტანეთ ერთად. 

# 2) მოცემული გაქვთ რაიმე result ცვლადი რომელშიც შეყვანილია სია [10,43,12,11,94,10,55,7,11] თქვენი დავალებაა გააქროთ ყველა დუბლიკატი ლისტიდან „თანმიმდევრობას მნიშვნელობა არაქვს“.

# 3) დღევანდელ ახსნილ მეთოდებზე გააკეთეთ მაგალითები თითო მეთოდზე 5 მაგალითი მაინც.

# 4) შექმენით ცარიელი dictionary შემდეგ მომხმარებელს შემოატანინეთ ჯერ key  შემდეგ კი value ამის შემდეგ თხოვეთ შეცვალოს ძველი value  და შემოატანინეთ ახალი მნიშვნელობა შემდეგ კი გამოიტანეთ საბოლოო dictionary.

# 5) შექმენით სეტის მსგავსი ფუნქცია რომელიც მიიღებს ლისტს და ლისტიდან წაშლის დუბლიკატებს „ფუნქციაში არ გამოიყენოთ სეტი“
#1
dict1 = {
    "bird": "eagle",
    "animals": "dog",
    "fish": "dolphin"
}
list1 = []
list2 = []
something = list1 + [dict1.keys()]
print(something)
something2 = list2 + [dict1.values()]
print(something2)
#2
result = [10,43,12,11,94,10,55,7,11]
print(set(result))
#3
dict2 = {
    "airport": "plane",
    "trainstation": "metro"
}
print(dict1.get("bird"))
print(dict1.get("animals"))
print(dict1.get("fish"))
print(dict2.get("airport"))
print(dict2.get("trainstation"))
print(dict1.keys())
print(dict1.values())
print(dict2.keys())
print(dict2.values())
print(dict1.items())
print(dict2.items())
#5
def no_dup(list):
    list = []
    for i in list:
        if i not in list:
            print(list.append(i))
