<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=C3B550&center=true&vCenter=true&width=600&lines=%F0%9F%91%BE+Internet+Speed+Reddit+Bot;%E2%9A%A1+Selenium+Automation;" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Automation-A9FEF7?style=for-the-badge&logo=robotframework&logoColor=black" height="35">
</div>

<br>

<h3>
  🚀 Project Overview<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

An automated Python script designed to hold internet service providers accountable. The bot runs a speed test, compares the results with your promised contract speeds, and automatically logs into Twitter to post a tweet directed at your provider if the speeds are below the guaranteed threshold.

**Key Features:**
* **🤖 Web Automation:** Uses `Selenium Webdriver` to navigate Speedtest.net and Twitter.
* **📊 Performance Analysis:** Extracts download and upload metrics in real-time.
* **🐦 Automated Tweeting:** Programmatically fills forms and interacts with Twitter's dynamic UI to post complaints.
* **🏗️ OOP Structure:** Built using a Class-based approach for clean and maintainable code.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
internet-speed-tester/
├── main.py                     # Main execution loop and logic
├── speed_bot.py                # InternetSpeedTwitterBot Class definition
└── .env                        # Credentials (Twitter Email/Pass/Provider)
```
<h3>
  🧠 Code Review & Complexity<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> **📊 SYSTEM COMPLEXITY RADAR**
>
> 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛ **90%** | **DOM Interaction (Selenium)**<br>
> 🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛ **70%** | **OOP Architecture (Classes)**<br>
> 🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛ **80%** | **Error Handling (Wait Times)**<br>
> 🟪🟪🟪🟪🟪⬛⬛⬛⬛⬛ **50%** | **Credential Management**

<br>

**🟢 High-Impact Wins:**
* **Bot Logic:** Excellent use of Object-Oriented Programming (OOP) to encapsulate the bot's behavior.
* **Element Targeting:** Successfully navigating complex, dynamic websites that use frequently changing CSS classes.

**🔧 Key Recommendations:**
* **Wait Strategies:** Use `WebDriverWait` (Explicit Waits) instead of `time.sleep()` to make the bot faster and more reliable on slow connections.
* **Headless Mode:** Add an option to run the Chrome driver in `--headless` mode so the bot can run in the background without opening a browser window.

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
