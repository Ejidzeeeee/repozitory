import matplotlib.pyplot as plt
import pandas as pd

def save_plot(filename):
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def generate_html_report(data, title="Отчёт", output="report.html"):
    if isinstance(data, pd.DataFrame):
        table_html = data.to_html()
    else:
        table_html = str(data)
    
    html = f"""
    <html>
    <head><title>{title}</title></head>
    <body>
    <h1>{title}</h1>
    {table_html}
    </body>
    </html>
    """
    with open(output, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Отчёт сохранён в {output}")
