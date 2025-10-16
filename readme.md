# 👻 SnapchatBoost

![snap1](https://github.com/user-attachments/assets/e632e18e-586d-48e4-b535-a830b5ac1405)

> ⚡ Automate Snapchat snap sending via **web.snapchat.com** using Python + GUI automation.  
> Created by **ohno**, for educational and productivity testing — **anonymous mode** edition.

---

## 🧠 Overview

`SnapchatBoost` is a desktop-based automation tool that interacts with **Snapchat Web** to automate repetitive snap-sending actions.  
It works by using `pyautogui` and `keyboard` to control the mouse and keyboard, simulating real interactions with the Snapchat interface.

This version includes:
- A **terminal interface with color animations**
- **ASCII startup banner and boot sequence**
- Configurable **delays, shortcut counts**, and **position mapping**
- **Time estimation** for automation batches
- Cross-platform support (Windows, macOS, Linux)

---

## 🚀 Features

| Feature | Description |
|----------|--------------|
| 🖱️ Mouse Position Mapping | Configure exact on-screen coordinates for all buttons (Camera, Send To, Shortcut, etc.) |
| ⚙️ Configurable Settings | Tune click and loop delays, shortcut size, etc. |
| ⏱️ Time Estimator | Calculate total run time for large snap batches |
| 💬 Pretty Console Output | Smooth typing animation with color-coded text |
| 🌍 Cross-Platform | Works on Windows, macOS, and Linux |
| 💡 Auto Help | Opens the GitHub README and Snapchat Web for convenience |

---

## 📦 Installation

### 🪟 Windows

**Easy installation (reccomended):**
- Press the green '**code**' button and click '**download zip**'
- Once it has downloaded **unzip** the file
- Double click the **install.bat** and wait until everything thing is installed
- You should see the display banner 

1. **Install Python (3.8 or newer):**
   - Download from [python.org/downloads](https://www.python.org/downloads/)
   - Or Download from the microsoft app store 
   - During install, check ✅ **“Add Python to PATH”**

2. **Open Command Prompt** and install dependencies:
   - Install pip by running
   ``` bash
   python3.10 -m ensurepip --default-pip
   ```
   and then running
   ``` bash
   pip install pyautogui keyboard colorama
