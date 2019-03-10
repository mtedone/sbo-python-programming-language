from abc import ABC, abstractmethod


def print_table(objects, colnames, formatter):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    :param objects: The list of objects
    :param colnames: The column names
    :return:
    '''

    if not isinstance(formatter, TableFormatter):
        raise TypeError('formatter must be a TableFormatter')

    formatter.headings(colnames)

    for obj in objects:
        # Emit a row of table data
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)


class TableFormatter(ABC):
    # Serves a design spec for making tables (use inheritance to customise)
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print('{:>10s}'.format(header), end=' ')
        print()

    def row(self, rowdata):
        for item in rowdata:
            print('{:>10s}'.format(item), end=' ')
        print()


class CVSTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        for h in headers:
            print('<th>{}</th>'.format(h), end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        for d in rowdata:
            print('<td>{}</td>'.format(d), end=' ')
        print('</tr>')
