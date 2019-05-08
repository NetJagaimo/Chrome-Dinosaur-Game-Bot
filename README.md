# 需求
你需要先安裝pillow、pyautogui以及mss套件

# 如何使用
1. 在chrome的網址列輸入"chrome://dino"打開遊戲
2. 調整"canvas.runner-canvas"的寬度為大約600，可以用F12開發者工具確認
3. 你需要輸入"canvas.runner-canvas"左上角的座標給程式，可以截圖下來貼到小畫家裡面確認該點座標

# 怎麼運作的
我使用mss去抓取小恐龍前方的特定區域，並使用pillow確認該區域內有幾種不同的顏色，如果多餘一種就使用pyautogui按下空白鍵讓小恐龍跳起。
使用顏色數量作為跳躍判斷的好處在於，不論是夜晚模式，或者是日夜交替時的漸層，它都可以處理。

# Requirements
You need to install "pillow", "pyautogui" and "mss" before run this program

# How to use
1. Open your chrome and input "chrome://dino" to the address bar to open the game
2. Make sure width of the "canvas.runner-canvas" is about 600, you can use F12 DevTools to check
3. Input the top left coordinate of "canvas.runner-canvas", you can print screen and paste to MS Paint to check the coordinates

# How it works
I'm use mss to grab a specfic area in front of the dinosaur, and use pillow check how many color is in this area. If there is more then one color, than use pyautogui to press the "space" so that the dinosaur will jump.
The advantage of use how many kinds of color in the area as the trigger is that it can handle night mode and gradual change between day and night.