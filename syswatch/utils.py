def format_bytes(size):
    for unit in ['', '', '', '']:
        if size < 1024:
            return f"{size: 2f} {unit}"
        size /= 1024