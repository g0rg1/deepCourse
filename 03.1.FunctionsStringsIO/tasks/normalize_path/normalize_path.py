def normalize_path(path: str) -> str:
    components = path.split('/')
    normalize_paths = []
    
    for component in components:
        if component == '.':
            continue
        elif component == '..':
            if normalize_paths:
                normalize_paths.pop()
        else:
            normalize_paths.append(component)
            
    normalized_path = '/' + '/'.join(normalize_paths)
    return normalized_path
            
