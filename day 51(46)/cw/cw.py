# 1) კომენტარის სახით ახსენით, თუ რა განასხვავებს tuple-ებს List-ებისგან.

# 2) შექმენით tuple, რომელიც შეიცავს თქვენს 5 საყვარელ ფილმს, შემდეგ კი დაბეჭდეთ პირველი და ბოლო ელემენტი ამ tuple-დან.

# 3) შემენით Tuple, რომელშიც შეინახავთ კვირის დღეებს და მოახდინეთ მათი unpacking (destruction),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.

# 4) შექმენით tuple, რომელიც შეიცავს რამდენიმე ელემენტს. შემდეგ შეამოწმეთ, შეიცავს თუ არა ეს tuple კონკრეტულ ელემენტს

# 5) მოცემულია Tuple = ["banana", "cherry", "strawberry", "raspberry"]
# (first, *second, third) = fruits

# რას გამოიტანს შემდეგი კოდი?
# print(first)
# print(second)
# print(third)
#tuple - almost just like a list but cannot be changed
#list - can be changed and its just a list
movie = ("paddington 3", "Sonic 3", "Mufasa 2", "The old man and the sea", "Willy Wonka")
print(movie[0], movie[-1])
week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
(first, second, third, fourth, fifth, sixth, seventh) = week
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
nums = (1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10)
first = "banana"
second = "cherry", "strawberry"
third = "raspberry"