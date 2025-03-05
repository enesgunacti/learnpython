lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Jim","Jim","Oscar","Toby"]

friends.extend(lucky_numbers) # listeye yeni elemanlar ekleme
friends.append("Creed") # liste sonuna eleman ekleme
friends.insert(1,"Keely") # x indeksine y verisini ekle
friends.remove("Jim")
#friends.clear()
friends.pop() # son elamanı siler => "Creed"

print(friends.index("Kevin"))
print(friends.count("Jim")) # yukarıda ilk => Jim'i sildiğini unutma count sayısı seni yanıltmasın
#print(friends.index("Mike")) # hata verir listede böyle birisi yok

friends = ["Kevin","Karen","Jim","Jim","Jim","Oscar","Toby"]

friends.sort() # sortdan önce listeyi güncelliyoruz çünkü içerisinde int değerler var. güncellemeden devam edersek int ve string değerleri aynı anda sort edemez.
lucky_numbers.sort()

print(friends)
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()

print(friends2)