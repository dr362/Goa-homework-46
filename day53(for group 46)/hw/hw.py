# ```2) კომენტარის სახით ჩამოწერეთ თუ რა განსხვავებაა set-ებსა და list-ებს შორის.

# 3) შექმენით set სადაც შეინახავთ რიცხვებს, შემდეგ კი ინდექსინგის საშუალებით სცადეთ თითოეული ელემენტის შეცვლა და დააკვირდით შედეგს.

# 4) შექმენით set, რომელშიც შენახული გექნებათ Fast food საკვები პროდუქტები. შემდეგ კი ამოშალეთ ყველა პირვანდელი ელემენტები set-იდან, და მათ ნაცვლად დაამატეთ ჯანსაღი საკვები პროდუქტები.

# 5) შექმენით ფუნქცია, რომელიც არგუმენტად იღებს სიას, და აბრუნებს იგივე სიას, მაგრამ დუპლიკატების გარეშე. hint: გააკეთეთ set-ის საშუალებით (output-ში ელემენტების თანმიმდევრობას მნიშვნელობა არ აქვს)

# test cases:

# list1 = [7, 5, 44, 14, 5, 5, 44]

# list2 = [89, 90, 56, 45, 90, 78, 90]```
#1)
    #list - its mutable can be used with indexes and alows duplicates
    #set - it doesen't alow duplicates and cannot be used with indexes
#2)
set1 = {1,2,4,6,6,9,10}
list(set1)
print(set1.add(11))
set(set1)
print(set1)
#3)
fastfood = {"cheeseburger","fries","mayoneese","ketchup","chips"}
print(fastfood.clear)
fastfood = {"soup","salad","fish","avocado","brocolli"}
print(fastfood)
#4)
def copy_of_list(list):
    set(list)
    copied = list.copy()
    print(copied)
    print(list)