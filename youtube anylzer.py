import pandas as pd 
import sqlite3
import requests
data = {
    "videos": [
        {"Title": "How to learn Python", "Views": 25000, "Likes": 1800, "Comments": 320, "UploadDate": "2024-05-01"},
        {"Title": "Data Analysis Project", "Views": 18000, "Likes": 1500, "Comments": 290, "UploadDate": "2024-05-05"},
        {"Title": "React JS tutorial", "Views": 15000, "Likes": 800, "Comments": 190, "UploadDate": "2024-05-08"},
        {"Title": "Instagram Clone", "Views": 12000, "Likes": 650, "Comments": 120, "UploadDate": "2024-05-10"},
        {"Title": "VS Code Tips", "Views": 27000, "Likes": 2200, "Comments": 350, "UploadDate": "2024-05-12"},
        {"Title": "Python Libraries", "Views": 30000, "Likes": 2500, "Comments": 410, "UploadDate": "2024-05-15"}
    ]
}
df=pd.DataFrame(data['videos'])
con=sqlite3.connect("youtube.db")
cur=con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        Title TEXT,
        Views INTEGER,
        Likes INTEGER,
        Comments INTEGER,
        UploadDate TEXT
        
    )
    ''')
df.to_sql('videos', con, if_exists='replace', index=False)
print("📦 Data stored in SQLite database successfully.")
print("\n🔥 Most Viewed Video:")
print(df.loc[df['Views'].idxmax()])
print("\n📤 Fetching from DB:")
df_db = pd.read_sql_query("SELECT * FROM videos", con)
print(df_db)
con.close()