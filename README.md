<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=39FF14&center=true&vCenter=true&width=600&lines=%F0%9F%91%BE+Internet+Speed+Reddit+Bot;%E2%9A%A1+Selenium+Automation;" alt="Animated Header" />
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
  <span style="color: #39FF14;">🚀 Project Overview</span><br>
  <img src="https://placehold.co/1000x2/39FF14/39FF14.png" width="100%" height="2" alt="Green Divider"/>
</h3>

An automated network monitoring tool built to hold Internet Service Providers accountable. The bot executes a real-time speed test and, if the results fall below the guaranteed contract speeds, it automatically logs into Reddit to post a complaint on the provider's official subreddit.

**Technical Logic (Verified):**
* **🤖 Multi-Domain Automation:** Orchestrates a complex Selenium workflow, moving from speed diagnostics on Speedtest.net to automated community engagement on Reddit.
* **🏗️ OOP Architecture:** Encapsulates the bot's state (down/up speeds) and behavior within a dedicated `InternetSpeedRedditBot` class for modularity.
* **🧠 Threshold-Based Triggers:** Implements logical comparisons between live metrics and contractually promised speeds to decide if a public post is necessary.
* **🔍 Reddit DOM Interaction:** Navigates Reddit's dynamic interface, handling login flows and automated form submission to post detailed performance reports.

<br>

<h3>
  <span style="color: #00E5FF;">📁 Project Structure</span><br>
  <img src="https://placehold.co/1000x2/00E5FF/00E5FF.png" width="100%" height="2" alt="Cyan Divider"/>
</h3>

```text
internet-speed-tester/
├── main.py                     # Workflow controller & logic gates
├── speed_bot.py                # InternetSpeedRedditBot Class definition
└── .env                        # Credentials (Reddit Login & ISP Thresholds)
```
<h3>
  <span style="color: #BC13FE;">🧠 Code Review & Complexity</span><br>
  <img src="https://placehold.co/1000x2/BC13FE/BC13FE.png" width="100%" height="2" alt="Purple Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=18&pause=1000&color=39FF14&vCenter=true&width=400&lines=>_ANALYZING_SYSTEM_COMPLEXITY..." alt="Animated Loading" />
> 
> <table>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">DOM Interaction (Selenium)</span></b></td>
>     <td width="200"><img src="https://placehold.co/180x10/39FF14/39FF14.png"/><img src="https://placehold.co/20x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">90%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #00E5FF;">OOP Architecture (Classes)</span></b></td>
>     <td width="200"><img src="https://placehold.co/140x10/00E5FF/00E5FF.png"/><img src="https://placehold.co/60x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #00E5FF;">70%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #BC13FE;">Handling Dynamic Pop-ups</span></b></td>
>     <td width="200"><img src="https://placehold.co/160x10/BC13FE/BC13FE.png"/><img src="https://placehold.co/40x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #BC13FE;">80%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">Automation Logic</span></b></td>
>     <td width="200"><img src="https://placehold.co/100x10/39FF14/39FF14.png"/><img src="https://placehold.co/100x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">50%</span></b></td>
>   </tr>
> </table>

<br>

**🟢 High-Impact Wins:**
* **Logic Decoupling:** Separating the speed diagnostic phase from the reporting phase ensures cleaner code.
* **Complex UI Handling:** Successfully identifying and interacting with Reddit's intricate login and posting elements.

**🔧 Technical Debt:**
* **Relative Selectors:** If Reddit updates its UI, the bot might need an update to its XPaths/CSS Selectors.
* **Headless Mode:** Running the bot without a visible UI (headless) would be a great production-ready improvement.

<br>

<br>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=16&duration=3000&pause=1000&color=00E5FF&center=true&vCenter=true&width=500&lines=[SYSTEM_SCAN_COMPLETE]----------------------------" alt="Animated Scan Divider" />
</div>
