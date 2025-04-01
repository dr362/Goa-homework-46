# ```
# 1) შექმენით დიქშენერი რომელშიც შეინახავთ თქვენი საყვარელი მანქანის აღწერას ბრენდის სახელს, მოდელსა და გამოშვების წელს შემდეგ დიქშენერიდან გამოიტანეთ გასაღებები და მნიშვნელობები წყვილად შემდეგ კი ცალ-ცალკე 

# 2)შექმენით 2 სეტი და ჯერ შეაერთეთ ერთმანეს შემდეგ გამოიტანეთ გნსხვავებები და მსგავსებები მათ შორის
 
# 3)შექმენით დიქშენერი რომლის მნიშვნელობებსაც გადაატარებთ forloop'ს და გამოიტანეთ ისინი ისინი

# 4)ახსენით დიქშენერი და სეტები კომენტარის სახით 
# 5)შექმენით dictionary და ცარიელი სია, შემდეგ for ციკლის მეშვოებით გადაუარეთ dictionary-ს და ჩაამატეთ მისი key და value-ბი სიაში

# 6)შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key / value წყვილს, შემდეგ მომხმარებელს შეეკითხეთ შემოიტანოს key და value, შემდეგ შეამოწმეთ თუ შექმნილ dict-ში არ გვაქვს მსგავსი key, მაშინ ჩაამატეთ ეს წყვილი, სხვა შემთხვევაში გამოიტანეთ "Key already exists!"
# ```
car = {
    "brand": "chevrolet",
    "model": "volt",
    "year": "2015"
}
print(car)
print(car.items())
#2
set = {"dog","cat","animal"}
set2 = {"cat","girrafe","animal"}
print(set.difference(set2))
#3 
dict1 = {
    "brand": "harley davidson",
    "model": "sportster s",
    "year": "2024"
}
for i in dict1:
    print(dict1)
#set - works almost like a list but dosen't allow any duplicates and cannot be used with indexes :)
#dictonary - ლექსიკონი (ინგლისურად აღწერის იდეები საერთოდ არ მქონდა)
#5
dict2 = {
    "programing language":"python",
    "site language?": "HTML",
    "game dev language": "LUA"
}
print(input("please enter any key and value: "))
if dict2.keys() != input:
    print(input + dict2)
else:
    print("KEY ALREADY EXISTS!")