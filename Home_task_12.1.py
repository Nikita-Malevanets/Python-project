import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
           html = html.replace('\n', '')
           cleaned_text = re.sub(r'<.*?>', '', html)
           cleaned_text = re.sub(r' +', ' ', cleaned_text)
           for element in ['.', '!', '?']:
               cleaned_text = cleaned_text.replace(f'{element}', f'{element}\n')

           cleaned_text = cleaned_text.splitlines()
           filtered_lines = []
           for line in cleaned_text:
               if line.strip():
                   filtered_lines.append(line)

           with open(result_file, 'w', encoding='utf-8') as file:
               file.write('\n'.join(filtered_lines))

delete_html_tags('draft.html')