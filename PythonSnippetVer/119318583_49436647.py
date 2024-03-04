import bonobo
def get_services():
    return {
        'fs.data': bonobo.open_fs('/data'),
    }
def get_graph():
    return bonobo.Graph(
        bonobo.CsvReader('input.csv', fs='fs.data'),
        ... # etc
    )

if __name__ == '__main__':
    bonobo.run(get_graph(), services=get_services())