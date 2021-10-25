# View images
import os
import re
listn = [x for x in os.listdir() if re.match(".*[.]jpg", x)]
print(listn)
print([x for x in os.walk("./")])