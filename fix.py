import re
with open("slides.md", "r", encoding="utf-8") as f:
    text = f.read()
pattern = re.compile(r"(?:[ \t]*<!-- Consistent indicator circle -->\n*)?[ \t]*<div class=\"absolute bottom-8 left-1/2[^\"]*\">\n[ \t]*<div class=\"indicator-circle\"></div>\n[ \t]*</div>")
rep = """<!-- Pagination Indicator -->\n<div class=\"absolute bottom-8 left-1/2 transform -translate-x-1/2 z-50 flex items-center justify-center gap-[12px]\">\n  <div v-for=\"i in $slidev.nav.total\" :key=\"i\"\n       class=\"w-[8px] h-[8px] rounded-full transition-all duration-300\"\n       :class=\"$slidev.nav.currentPage === i ? \"bg-[#8b5cf6] shadow-[0_0_12px_rgba(139,92,246,0.9)] scale-[1.3]\" : \"bg-[#1f1f2e]\"\">\n  </div>\n</div>"""
new_text = pattern.sub(rep, text)
with open("slides.md", "w", encoding="utf-8") as f:
    f.write(new_text)
print("Replaced instances:", len(pattern.findall(text)))
