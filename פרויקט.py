# בדיחה רנדומלית מתוך המאגר : 1
import requests
url= 'https://v2.jokeapi.dev/joke/Any'
response= requests.get(url)
data=response.json()
#בודק אם קיימת בדיחה ובמידה ולא מדפיס לי שלא נמצאה הבדיחה :תנאי if
if data['error']:
    print('joke not accepted')
#במידה ואין שגיאה ואכן קיימת הבדיחה
else :
   # אם הבדיחה מורכבת ממהלך אחד נקבל הדפסה של " בדיחה "
    if data['type']=='single':
        print(data['joke'])
    #במידה והבדיחה מורכבת משאלה ןתשובה נקבל הדפסה של השאלה בשורה נפרדת ושל הפאנץ בשורה שלאחר מכן
    else:
        print(data['setup'])
        print(data['delivery'])

#בדיחות לפי קטגוריה :2
import requests
# בכל פעם שנבחר קטגוריה נקבל בדיחה שנכללת באותה קטגוריית בדיחות
category = "programming"
#השתמשנו בf-str בכדי להוסיף את המשתנה שבו אנו מגדירים את הקטגוריה
# וכך הקישור יידע לאיזו סוג בדיחה לגשת בכל פעם שנריץ את הקוד
url = f"https://v2.jokeapi.dev/joke/{category}"
response= requests.get(url)
data=response.json()
if data['error']:
    print('joke not accepted')
else:
    print(data['category'])
    if data['type']=='single':
      print(data['joke'])
    else:
      print(data['setup'])
      print(data['delivery'])

#קוד עם טיפול בשגיאות :3
import requests
category = "Programming"
url = f"https://v2.jokeapi.dev/joke/{category}"
# מכניס את הקוד המסוכן לtry שיוכל להשאיר אותנו בקוד במידה ויש שגיאה
try:
    response = requests.get(url)
    data = response.json()

    if data["error"]:
        print("not found in this category")
    else:
        print(data["category"])
        if data["type"] == "single":
            print( data["joke"])
        else:
            print(data["setup"])
            print( data["delivery"])
# כאן אנו מגדירים את השגיאה שנרצה לטפל בה במידה והקוד ייפול , במקרה הזה במידה ויש שגיאת רשת כלומר
#שאין אינטרנט , השרת לא זמין וכדומה - הקוד לא ייפול ונקבל את ההודעה שהדפסנו
except requests.exceptions.RequestException as e:
    print("network error", e)