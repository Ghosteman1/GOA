#შექმენით სია, ამ სიაში ჩაწერეთ სხვადასხვა ციფრები (1, 2, 3, 4, ასე არა, რამე მაგ: 45, 23, 87, 55,) 
#და გამოიტანეთ ამ სიაში ყველა რიცხვის ჯამი, ასევე ამავე სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალ ცალკე, 
#და მიუწეროთ ლუწია თუ კენტი.



list = [24, 54, 19, 87, 65, 43, 75]
sum = 0
for i in list:
    sum +=i
print(sum)

for i in list:
    if i % 2 == 0:
        print(i, " even ")
    else:
        print(i," odd ")
    
    
    
    

