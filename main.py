import pandas


def csv_to_json(file, main_key, exclude, dest=None):
    """Convert data from csv file to json format, if dest is specified, create json file"""
    data_frame = pandas.read_csv(file)

    if dest is not None:
        return data_frame.groupby([main_key]).apply(column_handler, exclude=exclude).to_json(dest)
    else:
        return data_frame.groupby([main_key]).apply(column_handler, exclude=exclude).to_json()


def column_handler(data_frame, exclude):
    """"""
    dropped_columns = data_frame.drop(columns=exclude)
    column_list = list()
    for column in dropped_columns:
        column_list += (dropped_columns[column].to_list())
    return column_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_to_json(file='', main_key='',
                exclude=[''], dest='')

