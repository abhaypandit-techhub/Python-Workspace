
# REGULAR EXPRESSION

import re
text="The quick brown for jumps over the lazy dog. brown"

# search for a pattern

match=re.search("brown",text) # searching brown inside a text string
if match:
  print("match is found!")
  print("start index:",match.start())
  print("End  index:",match.end())

  # FIND ALL OCCURRENCE OF PATTERN

  matches=re.findall("the",text,re.IGNORECASE) # case insensitive search
  print("matches:",matches)

  # REPLACE A PATTERN

  new_text=re.sub("for","cat",text) #replacement
  print("New text:",new_text)