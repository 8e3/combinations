# Combination of Letters

This repository contains **simple lists of latin leters**, varying in length.📝  
The lists were generated using a **simple Python script**, the code for which can be found [**here**](https://github.com/8e3/combinations/blob/main/generator.py)!

<hr>

### Pregenerated lists in this repository:
- 1️⃣ Generic [**list**](https://github.com/8e3/combinations/blob/main/lists/1.txt) of every latin letter (26 lines, ~78 Bytes)
- 2️⃣ A [**list**](https://github.com/8e3/combinations/blob/main/lists/2.txt) of all possible **two / 2 character combinations** with latin letters (676 lines, ~2.64 Kilobytes)
- 3️⃣ A [**list**](https://github.com/8e3/combinations/blob/main/lists/3.txt) of all possible **three / 3 character combinations** with latin letters (17576 lines, ~85.8 Kilobytes)
- 4️⃣ A [**list**](https://github.com/8e3/combinations/blob/main/lists/4.txt) of all possible **four / 4 character combinations** with latin letters (456976 lines, ~2.61 Megabytes)
<br>

## What about longer combinations ⁉️

Sadly, due to GitHub's file size limitations I'm not able to provide any bigger lists. However you can **easily** create lists of **five, six, seven, eight, nine,** etcetera letter combinations on your own, following the steps below!

<br>

## Creating your own Lists, using my Script ❇️
###### ⚠️ Large lists take a significant amount of storage space & need more time to generate

#### Requirements:
- [**Python 3.x**](https://www.python.org/downloads/)
- Some sort of **Code- / Text-Editor**
  - [**PyCharm**](https://www.jetbrains.com/de-de/pycharm/) is recommended
- Enough disk space ;)

#### Steps to replicate:
1. **Download** the **Source Code** by heading [**here**](https://github.com/8e3/combinations/blob/main/generator.py) and pressing Control + Shift + S
2. **Open** the downloaded **Source Code** in your preferred **Code-Editor** <br> <sub>(For **PyCharm**, press **Control + O** in-app)</sub>
3. **Edit** the number at the end of **line 7**, which is set to 5 by default, to the length of your liking
4. Run the script:
   - If you are using **PyCharm**, simply click the ▶️ icon at the **top bar**, or press **Control + F5**. Once the list is done generating, the console will output a success message, similar to **"Process finished with exit code 0"**
   - If you are using a simple text editor (**on windows**), follow the **following** instructions:
       1. Open the location of the script in your **explorer**
       2. Click the path (Something like `This PC > Windows (C:) > User > Your_Name > Downloads`), if it isn't highlighted **double-click** it
       3. Type `CMD` and press **Enter**
       4. Inside of the newly opened **Command Prompt Window**, type `python generator.py` and press **Enter**
       5. Once the list is done generating, the Command Prompt will break lines.
5. **You successfully generated your own list of combinations** 🎉
