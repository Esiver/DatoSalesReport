import webbrowser
import dominate


def makeHtml(df):
    html_df = df.to_html
    dataTable = df.to_html('dataTable.html')
    print('made html')
    print(html_df)
    print('made html*******************')
    webbrowser.open('dataTable.html')
    print(dataTable)
    return dataTable

def orgHtml(df):
    f = open('newhtml.html','w')
    table = open('dataTable.html','r')
    html = f"""
        <html>
        <head>

        </head>
        <body>
        <h1>Data Analysis</h1>
        
        {table}
        </body>
        </html>
        """
    print(html)
    f.write(html)
    f.close()
    webbrowser.open('newhtml.html')
    return html

