import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re

text = "the quick red box"
pattern = r"the"

match = re.match(pattern, text)
if match:
    print("match found", match.group())



