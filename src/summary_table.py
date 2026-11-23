def format_markdown_table(headers, rows):
    hdr = '| ' + ' | '.join(headers) + ' |\n'
    sep = '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'
    body = ''.join(['| ' + ' | '.join(str(c) for c in r) + ' |\n' for r in rows])
    return hdr + sep + body
