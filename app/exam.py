import os


def find_all_html_files(s_dir, form, need):
    for root, dirs, files in os.walk(s_dir):
        for file in files:
            try:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        count_of_lines = sum(1 for line in f)
                        f.seek(0)
                        for i in range(count_of_lines):
                            content = f.readline().strip()
                            if content.startswith(form):
                                content2 = content.split('>')
                                if need not in content2[0]:
                                    print(f'Mistake in file {os.path.join(root, file)} in {i+1} line')
            except Exception as e:
                print(e)


search_dir = '/home/user595/PycharmProjects/test-i18n/app'
forms = ('<p', '<button', '<h2', '<h')
tag = 'i18n'


find_all_html_files(search_dir, forms, tag)
