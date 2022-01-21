import yaml

frame_path = 'king-gizzard.github.io/frame.html'
index_path = 'king-gizzard.github.io/index.html'
content_path = 'king-gizzard.github.io/source.yaml'

with open(frame_path, 'r') as f:
    frame = f.read().split('\n')

with open(content_path, 'r') as f:
    contents = yaml.load(f, Loader=yaml.Loader)

newsite = frame[0:15]

for cat,body in contents.items():
    newsite += [f'			<div class="icon">{body["icon"]}</div>']

for cat,body in contents.items():
    newsite += ['\t\t\t<div class="category">']
    for name,url in body['items'].items():
        newsite += [f'\t\t\t\t<li><a class="bm" href={url}>{name}</a></li>']
    newsite += ['\t\t\t</div>']

newsite += frame[-4:-1]

with open(index_path,'w') as f:
    [f.write(f'{i}\n') for i in newsite]

