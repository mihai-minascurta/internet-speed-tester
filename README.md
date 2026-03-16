<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=FF4500&center=true&vCenter=true&width=600&lines=%F0%9F%91%BE+Internet+Speed+Reddit+Bot;%E2%9A%A1+Selenium+Automation;" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Reddit_Automation-FF4500?style=for-the-badge&logo=reddit&logoColor=white" height="35">
</div>

<br>

<h3>
  🚀 Project Overview<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

An automated network monitoring tool built to hold Internet Service Providers accountable. The bot executes a real-time speed test and, if the results fall below the guaranteed contract speeds, it automatically logs into Reddit to post a complaint on the provider's official subreddit.

**Technical Logic (Verified):**
* **🤖 Multi-Domain Automation:** Orchestrates a complex Selenium workflow, moving from speed diagnostics on Speedtest.net to automated community engagement on Reddit.
* **🏗️ OOP Architecture:** Encapsulates the bot's state (down/up speeds) and behavior within a dedicated `InternetSpeedRedditBot` class for modularity.
* **🧠 Threshold-Based Triggers:** Implements logical comparisons between live metrics and contractually promised speeds to decide if a public post is necessary.
* **🔍 Reddit DOM Interaction:** Navigates Reddit's dynamic interface, handling login flows and automated form submission to post detailed performance reports.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
internet-speed-tester/
├── main.py                     # Workflow controller & logic gates
├── speed_bot.py                # InternetSpeedRedditBot Class definition
└── .env                        # Credentials (Reddit Login & ISP Thresholds)
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
> 🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛ **80%** | **Handling Dynamic Pop-ups**<br>
> 🟪🟪🟪🟪🟪⬛⬛⬛⬛⬛ **50%** | **Automation Logic**

<br>

**🟢 High-Impact Wins:**
* **Logic Decoupling:** Separating the speed diagnostic phase from the reporting phase ensures cleaner code.
* **Complex UI Handling:** Successfully identifying and interacting with Reddit's intricate login and posting elements.

**🔧 Technical Debt:**
* **Relative Selectors:** If Reddit updates its UI, the bot might need an update to its XPaths/CSS Selectors.
* **Headless Mode:** Running the bot without a visible UI (headless) would be a great production-ready improvement.

<br>

<div align="center">
  <img src="https://img.shields.io/badge/🤖_AI_Contribution-Project_HTML_%26_CSS-50FA7B?style=flat-square" alt="AI Note">
  <br>
  <samp style="font-size: 12px; color: #6272a4;">Any custom HTML/CSS used in this documentation's presentation was co-authored with AI.</samp>
</div>

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
