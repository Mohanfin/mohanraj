"""from scipy import stats
data=[10,10,20,30,40,50]
result=stats.mode(data)
print("mode=",result.mode[0])
print("count=",result.count[0])"""
from idlelib import browser

#pandas
"""import pandas as pd
s=pd.Series([1,2,3,4,4])
print(s)"""
#two dim column and row
"""import pandas as pd
data={'name':["ram","raji","raja"],'age':[20,30,40]}
df=pd.DataFrame(data)
print(df)"""
#queen
"""from collections import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
q.append(40)
print("queve",list(q))
print("remove","q.popleft()")
print("queve.after deterion:",list(q))"""
#web browser module
"""import webbrowser
webbrowser.open("https://cloudinary.com/tools/image-to-link")
webbrowser.open_new_tab("https://cloudinary.com/tools/image-to-link")
webbrowser.open_new_tab("https://cloudinary.com/tools/image-to-link"""
#image billow module
"""from pil import image
i=image("https://www.magnific.com/free-photos-vectors/beautiful")
i=i.rotation(10)
i=i.crop(50,50,100,200)
i.show()"""
#matplotlib.pyplotas plt
"""import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.title("graph")
plt.xlabel("x")
plt.ylabel("y") """
#bar chat
"""import matplotlib.pyplot as plt
course=["msc,mca,m.com"]
fees=[7000,8000,7800]
pit.bar(course,fees)
pit.title(college fees)
plt.xlabel("course")
plt.ylabel("frequence")
plt.show()"""
#pickle
import pickle
data={["name","raja","course","python","company","mnc"]}
with open("data.pkl","wb") as f:
    pickle.dump(data,f)
