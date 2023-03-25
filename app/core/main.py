from exam1 import *

file1 = "../view1/view1.html"
file2 = "../view2/view2.html"
file3 = "../view3/view3.html"

tag = ["p", "button", "h2", "h"]
marker = "i18n"

check_tag_in_html_file(tag, marker, file1)
check_tag_in_html_file(tag, marker, file2)
check_tag_in_html_file(tag, marker, file3)