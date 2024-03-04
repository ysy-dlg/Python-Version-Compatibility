import re 
template ="{0} likes {1}"
str_re = r"\w+"
re.search(template.format(str_re, str_re), ...) 