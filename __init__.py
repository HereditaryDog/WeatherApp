import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "d806712ca8563a707c49b28273b482c8"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showinfo("Error", "请输入城市名称")
        return
    full_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric&lang=zh_cn"
    response = requests.get(full_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        weather_info = f"城市: {city_name}\n温度: {temperature}°C\n天气状况: {weather}"
        result_label.config(text=weather_info)
    else:
        messagebox.showinfo("查询失败", "未能获取天气信息，请检查城市名称是否正确。")

# 创建主窗口
root = tk.Tk()
root.title("天气查询")

# 创建布局和控件
city_entry = tk.Entry(root)
city_entry.pack()

search_button = tk.Button(root, text="查询天气", command=get_weather)
search_button.pack()

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

# 启动事件循环
root.mainloop()
