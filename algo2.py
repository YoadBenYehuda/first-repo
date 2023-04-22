from datetime import date

def search(list, data):
    today = date.today() #הגדרת תאריך היום
    for i in list:
        #פתיחת רישמות עבודה
        current_short = []
        current_medium = []
        current_long = []
        #סיווג הדאטה לרשימות ע"פ מק"ט
        for n in data:
            if n["id"] == i["id"]:
                if n["date"] + 30 >= today:
                    current_short.append(n)
                elif n["date"] + 60 >= today:
                    current_medium.append(n)
                elif n["date"] + 180 >= today:
                    current_long.append(n)
        #חישוב מחיר עדכני לכל רשימה ע"י ממוצע משוקלל
        l1 = WAM(current_short)
        l2 = WAM(current_medium)
        l3 = WAM(current_long)
        #חישוב מחיר סופי ע"י ממוצע משוקלל
        final_price = WAM([i.price, l1, l2, l3])
        #עדכון רשימת המוצרים
        i[2] = final_price
    return list

#פונקצית ממוצע נע משוקלל
def WAM(list):
    sum = 0
    price_new = 0
    for i in range(1, (len(list)+1)):
        sum += i
    for i in range(1, (len(list)+1)):
        price_new += (list[i-1] * ((len(list)-i+1)/sum))
    return price_new
