<h1 align="center">Hi, I'm Meowmeowng 👋</h1>

<p align="center">
  <em>Junior Developer · Building tools that are actually useful</em>
</p>

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&amp;family=Barlow:wght@400;600&amp;display=swap" rel="stylesheet">

<div id="pst" style="
  max-width:380px;margin:1rem auto;background:#0b1f3a;border-radius:12px;
  overflow:hidden;font-family:'Barlow',sans-serif;color:#fff;
  box-shadow:0 8px 32px rgba(0,0,0,.45);
">
  <div style="height:3px;background:linear-gradient(90deg,#0038A8 33%,#CE1126 33% 66%,#FFD700 66%)"></div>

  <div style="display:flex;align-items:center;gap:10px;padding:10px 14px 8px">
    <img src="https://oras.pagasa.dost.gov.ph/images/pagasa_logo.png" alt="PH Flag" style="width:36px;border-radius:3px;border:1px solid rgba(255,255,255,.15)">
    <div style="flex:1;line-height:1.2">
      <div style="font-size:.62rem;letter-spacing:.1em;color:#FFD700;text-transform:uppercase">Philippine Standard Time</div>
      <div style="font-size:.7rem;color:rgba(255,255,255,.4)">UTC +8:00 · Asia/Manila</div>
    </div>
    <img src="https://oras.pagasa.dost.gov.ph/images/phil_flag.png" alt="PAGASA" style="width:34px;object-fit:contain">
  </div>
  
  <div style="text-align:center;padding:4px 10px 8px">
    <div style="display:flex;align-items:baseline;justify-content:center;gap:4px">
      <span id="pst-t" style="font-family:'Orbitron',monospace;font-size:clamp(1.4rem, 5vw, 2.0rem);font-weight:700;letter-spacing:.02em">PST</span>
      <span id="pst-ap" style="font-family:'Orbitron',monospace;font-size:.7rem;color:#FFD700;padding-bottom:1px">TIME</span>
    </div>
    <div id="pst-d" style="font-size:.65rem;color:rgba(255,255,255,.55);margin-top:1px;text-transform:uppercase;letter-spacing:.05em">MANILA, PHILIPPINES</div>
  </div>
</div>

<script>
(function(){
  function pad(n){return n<10?'0'+n:''+n}
  var M=['January','February','March','April','May','June','July','August','September','October','November','December'];
  var D=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  function tick(){
    var p=new Date(Date.now()+(new Date().getTimezoneOffset()+480)*60000);
    var h=p.getHours(),m=p.getMinutes(),s=p.getSeconds();
    document.getElementById('pst-t').textContent=pad(h%12||12)+':'+pad(m)+':'+pad(s);
    document.getElementById('pst-ap').textContent=h>=12?'PM':'AM';
    document.getElementById('pst-d').textContent=D[p.getDay()]+', '+M[p.getMonth()]+' '+p.getDate()+', '+p.getFullYear();
  }
  tick();setInterval(tick,1000);
})();
</script>
<p align="center">
  <a href="https://github.com/itszaheerlgs">
    <img src="https://img.shields.io/github/followers/itszaheerlgs?label=Follow&style=flat-square&color=4A90D9&labelColor=1a1a1a" />
  </a>
  <img src="https://komarev.com/ghpvc/?username=itszaheerlgs&style=flat-square&color=4A90D9&label=Profile+Views" />
</p>

---

### About Me

I'm a junior developer focused on building practical desktop tools and automation scripts. I enjoy working close to the metal — network utilities, video processing, and AI-powered applications.

- 🛠️ Currently building tools with **Python** and **CustomTkinter**
- 🤖 Integrating AI APIs into real workflows
- 🌱 Always learning — networking, computer vision, and backend development
- 📍 Philippines

---

### 🔧 Projects

| Project | Description | Stack |
|---|---|---|
| [**Titan Scanner**](https://github.com/itszaheerlgs/titanScanner) | Advanced LAN network scanner with port scanning, ARP spoofing detection, banner grabbing, and more | Python · Tkinter · Socket |
| [**Meownd Meme Maker**](https://github.com/itszaheerlgs/meownd-meme-maker) | GUI tool to composite any video (local or stream link) into a meme template — no editing needed | Python · MoviePy · OpenCV · yt-dlp |
| [**Yuichiro AI**](https://github.com/itszaheerlgs/yuichiro-ai) | Personal AI chat assistant with persistent memory, switchable personas, and TTS | Python · Groq · SQLite · CustomTkinter |

---

### 🧰 Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/CustomTkinter-1a1a1a?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/Groq_API-F55036?style=flat-square&logoColor=white" />
</p>

---

### 📊 GitHub Stats

<p align="center">
  <img src="https://streak-stats.demolab.com?user=itszaheerlgs&theme=default&hide_border=true&date_format=M%20j%5B%2C%20Y%5D&ring=4A90D9&fire=4A90D9&currStreakLabel=4A90D9" height="150" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=itszaheerlgs&theme=minimal&hide_border=true&color=4A90D9&line=4A90D9&point=4A90D9" />
</p>

---

<p align="center">
  <sub>Made with care · <a href="https://github.com/itszaheerlgs">github.com/itszaheerlgs</a></sub>
</p>
