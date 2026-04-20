import os
import re

dir_path = r"e:\marko-digital-marketing-agency-html-template-2025-10-11-02-57-29-utc\Marko v2 Main File\HTML_TEMPLATE"

with open(os.path.join(dir_path, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract header
header_match = re.search(r"<header>.*?</header>", index_content, re.DOTALL)
if header_match:
    header_str = header_match.group(0)

# Extract footer
footer_match = re.search(r"<footer.*?>.*?</footer>", index_content, re.DOTALL)
if footer_match:
    footer_str = footer_match.group(0)
    # The footer in index.html is sometimes inside <div class="bg-footer-wrapper"> without a <footer> tag?
    # Let's check if there is an actual <footer> tag.

# Let's verify footer structure manually just in case
