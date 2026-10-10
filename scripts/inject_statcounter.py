#!/usr/bin/env python3
"""Inject the existing robotics Statcounter tag into the exported JB2 HTML.

Matches the post-build publishing approach used by apuntes-python.
"""

from pathlib import Path

BUILD_DIR = Path("_build/html")
PROJECT_ID = "13211697"
SECURITY_CODE = "fb36e920"
MARKER = f"sc_project={PROJECT_ID}"

STATCOUNTER = f"""
<!-- Statcounter: Cinemática y dinámica de robots -->
<script type="text/javascript">
var sc_project={PROJECT_ID};
var sc_invisible=1;
var sc_security="{SECURITY_CODE}";
</script>
<script
  type="text/javascript"
  src="https://www.statcounter.com/counter/counter.js"
  async>
</script>
<noscript>
  <div class="statcounter">
    <a title="Web Analytics"
       href="https://statcounter.com/"
       target="_blank">
      <img class="statcounter"
           src="https://c.statcounter.com/{PROJECT_ID}/0/{SECURITY_CODE}/1/"
           alt="Web Analytics"
           referrerpolicy="no-referrer-when-downgrade">
    </a>
  </div>
</noscript>
<!-- End Statcounter -->
"""


def main():
    if not (BUILD_DIR / "index.html").is_file():
        raise FileNotFoundError(
            f"No HTML export found in {BUILD_DIR}. Run: jupyter book build --html"
        )

    modified = 0
    already_present = 0
    for path in BUILD_DIR.rglob("*.html"):
        content = path.read_text(encoding="utf-8")
        if MARKER in content:
            already_present += 1
            continue
        if "</body>" not in content:
            print(f"Skipping (no body closing tag): {path}")
            continue
        content = content.replace("</body>", f"{STATCOUNTER}\n</body>", 1)
        path.write_text(content, encoding="utf-8")
        modified += 1
        print(f"Injected Statcounter: {path}")

    if not modified and not already_present:
        raise RuntimeError("No HTML pages contain a Statcounter snippet.")
    print(f"Statcounter ready: {modified} inserted, {already_present} already present.")


if __name__ == "__main__":
    main()
