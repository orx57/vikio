%if name == 'World':
    Hello **{{name}}**, how are you?
%else:
    Hello **{{name.title()}}**, how are you?
%end
