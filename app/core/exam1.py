from bs4 import BeautifulSoup


def check_tag_in_html_file(tag, marker, file):
    with open(file, "r", encoding="utf-8") as f:
        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        for tag in soup.find_all(tag):
            if not tag.has_attr(marker):
                print(f"{tag} is unmarked '{marker}' in {file} ")


