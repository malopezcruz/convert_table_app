def process_html(soup, caption_text):
    
    # Find the table element
    table = soup.find('table')

    # Create thead if it doesn't exist
    thead = soup.find('thead')
    if not thead:
        thead = soup.new_tag('thead')
        first_row = soup.find('tr')
        first_row.extract()

        # Convert all td elements to th
        for td in first_row.find_all('td'):
            td.name = 'th'

        thead.append(first_row)
        table.insert(0, thead)

    # Add class to thead
    thead['class'] = 'thead'

    # Remove class from thead tr
    thead_tr = thead.find('tr')
    if 'class' in thead_tr.attrs:
        del thead_tr.attrs['class']

    # Add scope="col" to the header cells in thead
    header_cells = thead.select('tr th')
    for cell in header_cells:
        cell['scope'] = 'col'

    # Find tbody
    tbody = soup.find('tbody')
    if not tbody:
        tbody = soup.new_tag('tbody')
        table.append(tbody)

    # Add scope="row" to the first td of each row in tbody and convert it to th
    body_rows = soup.select('tbody tr')
    for index, row in enumerate(body_rows):
        # Add even and odd classes to the rows
        if index % 2 == 0:
            row['class'] = 'even'
        else:
            row['class'] = 'odd'

        first_td = row.find('td')
        if first_td:
            first_td.name = 'th'
            first_td['scope'] = 'row'

    # Check if the last row contains "total"
    last_row = body_rows[-1]
    contains_total = "total" in last_row.get_text().lower()

    # Move the last row containing "total" to tfoot and create it
    tfoot = None
    if contains_total:
        last_row.extract()
        tfoot = soup.new_tag('tfoot')
        tfoot.append(last_row)
        table.insert(2, tfoot)

        # Add class to tfoot
        tfoot['class'] = 'tfoot'

        # Remove class from tfoot tr
        tfoot_tr = tfoot.find('tr')
        if 'class' in tfoot_tr.attrs:
            del tfoot_tr.attrs['class']
    
    # Add a caption to the table
    caption = soup.new_tag('caption')
    caption.string = caption_text
    caption['class'] = 'hidden'
    table.insert(0, caption)

    # Add role="table" to the table tag
    table['role'] = 'table'
