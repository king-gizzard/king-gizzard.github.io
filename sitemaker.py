import yaml
import re

frame_path = 'frame.html'
index_path = 'index.html'
content_path = 'source.yaml'
style_path = 'style.css'

def read_file(path):
    if path.split('.')[-1] == 'yaml':
        with open(content_path, 'r') as f:
            x = yaml.load(f, Loader=yaml.Loader)
    else:
        with open(path,'r') as f:
            x = f.read().split('\n')
    return(x)

def write_file(path, text):
    with open(path,'w') as f:
        [f.write(f'{i}\n') for i in text]

frame = read_file(frame_path)
contents = read_file(content_path)
style = read_file(style_path)

#sandwich contents in-between frame buns
#and mash together with frame-salad
newsite = frame[0:15]
for cat,body in contents.items():
    newsite += [f'			<div class="icon">{body["icon"]}</div>']
for cat,body in contents.items():
    newsite += ['\t\t\t<div class="category">']
    for name,url in body['items'].items():
        newsite += [f'\t\t\t\t<li><a class="bm" href={url}>{name}</a></li>']
    newsite += ['\t\t\t</div>']
newsite += frame[-4:-1]

write_file(index_path, newsite)

#correct the number of columns used in style-css
col_def_row = [r for r in style if 'grid-template-columns' in r][0]
col_def_index = style.index(col_def_row)
#col_def_row[-7] = len(contents.keys())
style[col_def_index] = re.sub(
        r'[0-9],1fr',
        f'{len(contents.keys())},1fr'
        ,col_def_row)

write_file(style_path, style)
