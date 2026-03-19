---
theme: default
class: text-center bg-[#050510]
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: fade

fonts:
  sans: "Montserrat"
  custom: "Oswald"

# Aspect ratio for your presentation
aspectRatio: 16/9
---

<div class="w-full h-full flex flex-col items-center justify-center bg-[#050510]">
  <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mb-2 font-semibold">
    Databases 101
  </p>
  <h1 class="text-[3rem] font-bold tracking-[-0.02em] leading-tight">
    <span class="neon-cool">DITCH THE ANCIENT SQL SCROLLS FOR</span>
    <span class="neon-warm">SQLMODEL</span>
  </h1>
  <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mb-2 font-semibold">
    Christian Mark P. Francisco
  </p>
</div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6; /* Matches the middle purple of your neon-cool */
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}
</style>

---
layout: default
class: "!p-0 bg-[#050510]"
clicks: 1
---

<div class="relative w-full h-full overflow-hidden bg-[#050510]">
  <div class="absolute inset-0 pointer-events-none">
    <div
      class="absolute inset-0"
      style="
        background:
          radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
          radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
          #050510;
      "
    ></div>
  </div>

  <div class="relative z-10 h-full flex flex-col items-center justify-center px-16 md:px-20 text-center w-full">
    <div class="max-w-5xl flex flex-col items-center justify-center">
      <p
        class="text-[2.25rem] leading-tight tracking-tight text-[#d1d5db] transition-all duration-700"
        :class="$slidev.nav.clicks >= 1 ? 'opacity-45 line-through decoration-2 decoration-[#9ca3af]' : 'opacity-100'"
      >
        The world revolves around data.
      </p>
      <p
        v-click="1"
        class="mt-5 text-[2.5rem] leading-tight font-bold tracking-tight uppercase"
      >
        <span class="neon-cool">Data runs</span>
        <span class="neon-warm">the world.</span>
      </p>
    </div>
  </div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6; /* Matches the middle purple of your neon-cool */
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}
</style>

---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full overflow-hidden bg-[#050510]">
  <!-- Consistent corner glows -->
  <div class="absolute inset-0 pointer-events-none">
    <div
      class="absolute inset-0"
      style="
        background:
          radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
          radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
          #050510;
      "
    ></div>
  </div>

  <div class="relative z-10 w-full h-full flex flex-col items-center justify-center bg-transparent px-14">
    <div class="max-w-4xl flex flex-col items-center justify-center">
      <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mb-2 font-semibold">
        Databases 101
      </p>
      <h1 class="text-[3rem] font-bold tracking-[-0.02em] leading-tight text-center">
        <span class="neon-cool">DITCH THE ANCIENT SQL SCROLLS FOR</span><br/>
        <span class="neon-warm">SQLMODEL</span>
      </h1>
      <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mt-2 font-semibold">
        Christian Mark P. Francisco
      </p>
    </div>
  </div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6; /* Matches the middle purple of your neon-cool */
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}
</style>

---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full overflow-hidden bg-[#050510]">
  <!-- Consistent corner glows -->
  <div class="absolute inset-0 pointer-events-none">
    <div
      class="absolute inset-0"
      style="
        background:
          radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
          radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
          #050510;
      "
    ></div>
  </div>

  <div class="relative z-10 h-full flex flex-col items-center justify-center px-16 md:px-20 text-center w-full">
    <div class="max-w-5xl flex flex-col items-center justify-center">
      <h1 class="text-[4.5rem] font-bold tracking-tight leading-none mb-6">
        <span class="neon-cool">DATABASES</span>
      </h1>
      <p class="text-xl md:text-2xl text-gray-400 font-light max-w-2xl leading-relaxed">
        Where the computer stores data
      </p>
    </div>
  </div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full bg-[#050510]">
  <!-- Consistent corner glows -->
  <div class="absolute inset-0 pointer-events-none">
    <div
      class="absolute inset-0"
      style="
        background:
          radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
          radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
          #050510;
      "
    ></div>
  </div>

  <div class="relative z-10 w-full h-full flex flex-col items-center pt-24 px-16">
    <!-- Header mirroring 'Four Critical Questions' layout -->
    <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mb-2 font-semibold text-center">
      THE TRADITIONAL APPROACH
    </p>
    <h1 class="text-[3rem] font-bold tracking-[-0.02em] leading-tight mb-8 text-center">
      <span class="neon-cool">DATABASES WITH</span>
      <span class="neon-warm"> PYTHON.</span>
    </h1>
    <!-- Card containing the Monaco editor, mimicking the grid cards -->
    <div class="w-full max-w-4xl bg-[#0a0a16]/80 backdrop-blur-sm rounded-xl border border-[#4f46e5]/30 flex flex-col shadow-[0_0_30px_rgba(79,70,229,0.1)] mb-[100px]">
      <div class="px-5 py-3 border-b border-[#4f46e5]/20 flex items-center">
        <span class="text-[0.65rem] text-[#6b8cff] uppercase tracking-widest font-semibold flex-shrink-0">01</span>
        <span class="text-xs font-mono text-[#a1a1aa] ml-3 tracking-wide font-semibold">SQLITE3 DEMO (THE NORMAL WAY)</span>
      </div>
      <div class="p-1 text-left text-lg overflow-y-auto min-h-[150px] h-[200px]">

```python {monaco-run}
# Demo here
```
</div>
</div>
</div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6; /* Matches the middle purple of your neon-cool */
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}

/* Make Monaco Editor blend into our neon glassmorphism card! */
.slidev-monaco-container {
  min-height: 280px !important;
  max-height: 380px !important;
  height: 100% !important;
  display: flex;
  flex-direction: column;
}
.slidev-monaco-container .monaco-wrapper,
.slidev-monaco-container .monaco-editor {
  flex-grow: 1 !important;
  height: 100% !important;
  min-height: 280px !important;
}
.slidev-monaco-container,
.monaco-wrapper,
.monaco-editor,
.monaco-editor-background,
.monaco-editor .margin,
.monaco-editor .monaco-scrollable-element {
  background-color: transparent !important;
  --slidev-code-background: transparent !important;
}
.monaco-editor .view-overlays .current-line {
  background-color: rgba(139, 92, 246, 0.15) !important; /* Soft purple glow for the selected line */
  border: none !important;
}
.monaco-editor .margin-view-overlays .current-line-margin {
  background-color: transparent !important;
  border: none !important;
}
</style>

---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full overflow-hidden bg-[#050510]">
  <!-- Consistent corner glows -->
  <div class="absolute inset-0 pointer-events-none">
    <div
      class="absolute inset-0"
      style="
        background:
          radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
          radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
          #050510;
      "
    ></div>
  </div>

  <div class="relative z-10 w-full h-full flex flex-col items-center justify-center bg-transparent px-14">
    <div class="max-w-5xl flex flex-col items-center justify-center">
      <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mb-4 font-semibold text-center">
        What if we can just use
      </p>
      <h1 class="text-[4rem] font-bold tracking-[-0.02em] leading-tight text-center">
        <span class="neon-warm">PURE PYTHON</span>
      </h1>
      <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mb-4 font-semibold text-center">
        instead
      </p>
    </div>
  </div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6; /* Matches the middle purple of your neon-cool */
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}

/* Make Monaco Editor blend into our neon glassmorphism card! */
.slidev-monaco-container {
  min-height: 280px !important;
  max-height: 380px !important;
  height: 100% !important;
  display: flex;
  flex-direction: column;
}
.slidev-monaco-container .monaco-wrapper,
.slidev-monaco-container .monaco-editor {
  flex-grow: 1 !important;
  height: 100% !important;
  min-height: 280px !important;
}
.slidev-monaco-container,
.monaco-wrapper,
.monaco-editor,
.monaco-editor-background,
.monaco-editor .margin,
.monaco-editor .monaco-scrollable-element {
  background-color: transparent !important;
  --slidev-code-background: transparent !important;
}
.monaco-editor .view-overlays .current-line {
  background-color: rgba(139, 92, 246, 0.15) !important; /* Soft purple glow for the selected line */
  border: none !important;
}
.monaco-editor .margin-view-overlays .current-line-margin {
  background-color: transparent !important;
  border: none !important;
}
</style>

---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full overflow-hidden bg-[#050510]">
  <!-- Consistent corner glows -->
  <div class="absolute inset-0 pointer-events-none">
    <div
      class="absolute inset-0"
      style="
        background:
          radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
          radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
          #050510;
      "
    ></div>
  </div>

  <div class="relative z-10 w-full h-full flex flex-col items-center justify-center bg-transparent px-14">
    <div class="max-w-5xl flex flex-col items-center justify-center">
      <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mb-4 font-semibold text-center">
        How does it work?
      </p>
      <h1 class="text-[3rem] font-bold tracking-[-0.02em] leading-tight text-center mb-6">
        <span class="neon-cool">OBJECT-RELATIONAL MAPPING </span>
        <span class="neon-warm">(ORM)</span>
      </h1>
      <p class="text-xl md:text-2xl text-gray-400 font-light max-w-3xl leading-relaxed text-center mb-10">
        Lets us represent database tables as <span class="text-[#6b8cff] font-semibold">Python classes</span>.
      </p>
      <div class="w-full max-w-4xl flex items-center justify-center gap-4 mt-2">
        <!-- Python Code Card -->
        <div class="flex-1 bg-[#0a0a16]/80 backdrop-blur-sm border border-[#6b8cff]/40 rounded-xl py-6 px-4 flex flex-col items-center justify-center shadow-[0_0_20px_rgba(107,140,255,0.15)]">
          <span class="text-3xl mb-3">ðŸ</span>
          <span class="text-[#6b8cff] font-bold text-sm tracking-widest mb-1">PYTHON CODE</span>
          <span class="text-[0.65rem] text-[#6b7280] font-mono">Standard classes</span>
        </div>

<!-- Arrow -->
<div class="text-[#6b8cff] opacity-60">
<svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
</svg>
</div>

<!-- ORM Card -->
<div class="flex-1 bg-[#0a0a16]/80 backdrop-blur-sm border border-[#f6ad55]/40 rounded-xl py-6 px-4 flex flex-col items-center justify-center shadow-[0_0_20px_rgba(246,173,85,0.15)]">
    <span class="text-3xl mb-3">ðŸ”—</span>
    <span class="text-[#f6ad55] font-bold text-sm tracking-widest mb-1 text-center">SQLMODEL (ORM)</span>
    <span class="text-[0.65rem] text-[#6b7280] font-mono">Mapping layer</span>
</div>

<!-- Arrow -->
<div class="text-[#f6ad55] opacity-60">
<svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
</svg>
</div>

<!-- Database Card -->
<div class="flex-1 bg-[#0a0a16]/80 backdrop-blur-sm border border-[#c084fc]/40 rounded-xl py-6 px-4 flex flex-col items-center justify-center shadow-[0_0_20px_rgba(192,132,252,0.15)]">
    <span class="text-3xl mb-3">ðŸ—„ï¸</span>
    <span class="text-[#c084fc] font-bold text-sm tracking-widest mb-1 text-center">DATABASE (SQL)</span>
    <span class="text-[0.65rem] text-[#6b7280] font-mono">Persistent storage</span>
</div>
</div>

</div>
</div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6;
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}
</style>

---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full overflow-hidden bg-[#050510]">
<!-- Consistent corner glows -->
<div class="absolute inset-0 pointer-events-none">
<div
class="absolute inset-0"
style="
background:
radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
#050510;
"
></div>
</div>

<div class="relative z-10 w-full h-full flex flex-col items-center justify-center bg-transparent px-14">
<!-- 2-Column Layout Container -->
<div class="w-full max-w-6xl grid grid-cols-12 gap-8 items-center flex-grow py-6 px-8">

<!-- Left Column: Intro Text -->
<div class="col-span-12 md:col-span-5 flex flex-col justify-center text-left">
<p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b8cff] mb-3 font-semibold flex items-center gap-2">
<span class="w-1.5 h-1.5 rounded-full bg-[#6b8cff]"></span> THE FRAMEWORK
</p>
<h1 class="text-[2.5rem] font-bold tracking-tight leading-none mb-4">
<span class="text-white uppercase block">The Sorcerer's</span>
<span class="neon-cool uppercase block mt-1">Tool.</span>
</h1>
<div class="h-[1px] w-10 bg-gray-800 mb-4"></div>
<p class="text-xs md:text-[0.8rem] text-gray-400 font-light leading-relaxed mb-3">
SQLModel is a modern library designed to make database interactions feel like 
<strong class="text-[#f6ad55] font-medium block mt-1 w-max px-2 py-0.5 rounded bg-[#f6ad55]/10 border border-[#f6ad55]/20">Regular Python Code</strong>
</p>
</div>

<!-- Right Column: Features Grid -->
<div class="col-span-12 md:col-span-7 flex flex-col space-y-2 max-h-[60vh] overflow-y-auto pr-2 custom-scrollbar mask-edges">
<div class="py-1 flex flex-col space-y-2 w-full">
<!-- Feature 1 -->
<div class="w-full bg-[#0a0a16]/60 rounded-md border border-gray-800/60 border-l-[3px] border-l-[#6b8cff] flex py-2 px-3 items-center gap-3 shadow-sm shrink-0">
<div class="text-[#6b8cff] text-lg" i-carbon-idea></div>
<div class="text-left flex-1">
<div class="text-[#6b8cff] font-bold tracking-widest text-[0.7rem] mb-0.5 uppercase">Built by Tiangolo</div>
<p class="text-gray-500 text-[0.65rem] font-mono leading-relaxed m-0">From the creator of FastAPI, ensuring top-tier developer experience.</p>
</div>
</div>

<!-- Feature 2 -->
<div class="w-full bg-[#0a0a16]/60 rounded-md border border-gray-800/60 border-l-[3px] border-l-[#f6ad55] flex py-2 px-3 items-center gap-3 shadow-sm shrink-0">
<div class="text-[#f6ad55] text-lg" i-carbon-code></div>
<div class="text-left flex-1">
<div class="text-[#f6ad55] font-bold tracking-widest text-[0.7rem] mb-0.5 uppercase">Pythonic First</div>
<p class="text-gray-500 text-[0.65rem] font-mono leading-relaxed m-0">Uses standard Type Hints to define your database schema.</p>
</div>
</div>

<!-- Feature 3 -->
<div class="w-full bg-[#0a0a16]/60 rounded-md border border-gray-800/60 border-l-[3px] border-l-[#c084fc] flex py-2 px-3 items-center gap-3 shadow-sm shrink-0">
<div class="text-[#c084fc] text-lg" i-carbon-data-base></div>
<div class="text-left flex-1">
<div class="text-[#c084fc] font-bold tracking-widest text-[0.7rem] mb-0.5 uppercase">Single Source of Truth</div>
<p class="text-gray-500 text-[0.65rem] font-mono leading-relaxed m-0">One model for both validation and database management.</p>
</div>
</div>

<!-- Extra Box to Match Reference Style -->
<div class="w-full bg-[#0a0a16]/60 rounded-md border border-gray-800/60 border-l-[3px] border-l-[#10b981] flex py-2 px-3 items-center gap-3 shadow-sm shrink-0 mt-1">
<div class="text-[#10b981] text-lg" i-carbon-checkmark></div>
<div class="text-left flex-1">
<div class="text-[#10b981] font-bold tracking-widest text-[0.7rem] mb-0.5 uppercase">Solution: Enterprise Ready</div>
<p class="text-gray-500 text-[0.65rem] font-mono leading-relaxed m-0">Combines Python models directly with the robust SQLAlchemy core.</p>
</div>
</div>
</div>
</div>

</div>
</div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6;
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}

.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.1); 
  border-radius: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(139, 92, 246, 0.3); 
  border-radius: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(139, 92, 246, 0.6); 
}

.mask-edges {
  mask-image: linear-gradient(to top, transparent 0%, black 5%);
  -webkit-mask-image: linear-gradient(to top, transparent 0%, black 5%);
}
</style>

---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full bg-[#050510]">
  <!-- Consistent corner glows -->
  <div class="absolute inset-0 pointer-events-none">
    <div
      class="absolute inset-0"
      style="
        background:
          radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
          radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
          #050510;
      "
    ></div>
  </div>

  <div class="relative z-10 w-full h-full flex flex-col items-center pt-24 px-16">
    <!-- Header mirroring 'Four Critical Questions' layout -->
    <p class="text-[0.6rem] uppercase tracking-[0.4em] text-[#6b7280] mb-2 font-semibold text-center">
      THE NEW PYTHONIC WAY
    </p>
    <h1 class="text-[3rem] font-bold tracking-[-0.02em] leading-tight mb-8 text-center">
      <span class="neon-cool">DATABASES WITH</span>
      <span class="neon-warm"> PYTHON.</span>
    </h1>
    <!-- Card containing the Monaco editor, mimicking the grid cards -->
    <div class="w-full max-w-4xl bg-[#0a0a16]/80 backdrop-blur-sm rounded-xl border border-[#4f46e5]/30 flex flex-col shadow-[0_0_30px_rgba(79,70,229,0.1)] mb-[100px]">
      <div class="px-5 py-3 border-b border-[#4f46e5]/20 flex items-center">
        <span class="text-[0.65rem] text-[#6b8cff] uppercase tracking-widest font-semibold flex-shrink-0">01</span>
        <span class="text-xs font-mono text-[#a1a1aa] ml-3 tracking-wide font-semibold">SQLMODEL DEMO (MODERN WAY)</span>
      </div>
      <div class="p-1 text-left text-lg overflow-y-auto min-h-[150px] h-[200px]">

```python {monaco-run}
# Demo here
```
</div>
</div>
</div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6; /* Matches the middle purple of your neon-cool */
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}

/* Make Monaco Editor blend into our neon glassmorphism card! */
.slidev-monaco-container {
  min-height: 280px !important;
  max-height: 380px !important;
  height: 100% !important;
  display: flex;
  flex-direction: column;
}
.slidev-monaco-container .monaco-wrapper,
.slidev-monaco-container .monaco-editor {
  flex-grow: 1 !important;
  height: 100% !important;
  min-height: 280px !important;
}
.slidev-monaco-container,
.monaco-wrapper,
.monaco-editor,
.monaco-editor-background,
.monaco-editor .margin,
.monaco-editor .monaco-scrollable-element {
  background-color: transparent !important;
  --slidev-code-background: transparent !important;
}
.monaco-editor .view-overlays .current-line {
  background-color: rgba(139, 92, 246, 0.15) !important; /* Soft purple glow for the selected line */
  border: none !important;
}
.monaco-editor .margin-view-overlays .current-line-margin {
  background-color: transparent !important;
  border: none !important;
}
</style>
---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full overflow-hidden bg-[#050510]">
<!-- Consistent corner glows -->
<div class="absolute inset-0 pointer-events-none">
<div
class="absolute inset-0"
style="
background:
radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
#050510;
"
></div>
</div>

<div class="relative z-10 w-full h-full flex flex-col items-center justify-center bg-transparent px-14">
<div class="max-w-5xl flex flex-col items-center justify-center">
<h1 class="text-[4.5rem] font-bold tracking-tight leading-loose text-center">
  <span class="neon-warm uppercase tracking-widest text-[1.8rem] block mb-2 opacity-90">THANKS TO SQLMODEL,</span>
  <span class="text-white">No more </span>
  <span class="font-mono text-gray-500 line-through decoration-[#ef4444] decoration-[8px]">rows[0][1]</span>
</h1>
</div>
</div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6;
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}
</style>

---
layout: default
class: "!p-0 bg-[#050510]"
---

<div class="relative w-full h-full overflow-hidden bg-[#050510]">
<!-- Consistent corner glows -->
<div class="absolute inset-0 pointer-events-none">
<div
class="absolute inset-0"
style="
background:
radial-gradient(60rem 40rem at -8% -10%, rgba(79, 70, 229, 0.30) 0%, rgba(79, 70, 229, 0.00) 65%),
radial-gradient(65rem 45rem at 108% 110%, rgba(245, 158, 11, 0.22) 0%, rgba(245, 158, 11, 0.00) 68%),
#050510;
"
></div>
</div>

<div class="relative z-10 w-full h-full flex flex-col items-center justify-center bg-transparent px-14 py-4">

<div class="flex flex-col items-center justify-center mb-6 mt-2">
<h1 class="text-[4rem] font-bold tracking-tight leading-none text-center">
<span class="neon-cool uppercase">QUESTIONS?</span>
</h1>
<div class="h-[3px] w-24 bg-[#10b981] mt-4 rounded-full shadow-[0_0_15px_rgba(16,185,129,0.5)]"></div>
</div>

<div class="w-full max-w-4xl grid grid-cols-2 gap-10 mb-8 px-6">

<!-- Final Wisdom Column -->
<div class="flex flex-col">
<h3 class="text-[#6b8cff] font-bold tracking-widest text-[0.95rem] mb-4 uppercase text-left">Final Wisdom</h3>
<ul class="space-y-4">
<li class="flex items-center gap-3 text-gray-300">
<div class="text-[#10b981] text-xl" i-carbon-document></div>
<p class="text-[0.9rem] m-0">Official Docs: <span class="text-[#10b981] font-mono">sqlmodel.tiangolo.com</span></p>
</li>
<li class="flex items-center gap-3 text-gray-300">
<div class="text-[#10b981] text-xl" i-carbon-branch></div>
<p class="text-[0.9rem] m-0">Check out the FastAPI integration.</p>
</li>
</ul>
</div>

<!-- Next Steps Column -->
<div class="flex flex-col">
<h3 class="text-[#f6ad55] font-bold tracking-widest text-[0.95rem] mb-4 uppercase text-left">Next Steps</h3>
<ul class="space-y-4">
<li class="flex items-center gap-3 text-gray-300">
<div class="text-[#10b981] text-xl" i-carbon-education></div>
<p class="text-[0.9rem] m-0">Build a simple "Hero" API.</p>
</li>
<li class="flex items-center gap-3 text-gray-300">
<div class="text-[#10b981] text-2xl" i-carbon-magic-wand></div>
<p class="text-[0.9rem] m-0">Cast your first database spell!</p>
</li>
</ul>
</div>

</div>

<!-- Banner -->
<div class="w-full max-w-3xl bg-[#10b981]/10 border-2 border-[#10b981]/50 rounded-xl py-2 px-6 flex justify-center items-center shadow-[0_0_30px_rgba(16,185,129,0.2)] transform hover:scale-105 transition-transform duration-300">
<div class="text-white font-bold tracking-widest text-[0.8rem] m-0 uppercase text-center">
Go Forth And Cast Your <span class="text-[#10b981]">Database Spells!</span>
</div>
</div>

</div>

  <!-- Pagination Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[14px]">
    <div v-for="i in $slidev.nav.total" :key="i" class="w-[7px] h-[7px] rounded-full transition-all duration-300" :class="$slidev.nav.currentPage === i ? 'bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,1)] scale-[1.4]' : 'bg-[#2a2a3a]'"></div>
  </div>
</div>

<style>
.neon-cool {
  font-family: "Oswald";
  background: linear-gradient(to right, #6b8cff, #8b5cf6, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(107, 140, 255, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
  padding-right: 0.2em;
}
.neon-warm {
  font-family: "Oswald";
  background: linear-gradient(to right, #fbd38d, #f6ad55, #ed8936);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 20px rgba(246, 173, 85, 0.4), 0 0 40px rgba(237, 137, 54, 0.2);
}

.indicator-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #8b5cf6;
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.8), 0 0 20px rgba(139, 92, 246, 0.6);
}
</style>
