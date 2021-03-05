import clickhouse_driver

from common.classes import Job


class ClickHouse(Job):

    def __init__(self, *args, **kwargs):
        super(ClickHouse, self).__init__(*args, **kwargs)

    def do_backup(self):
        client = clickhouse_driver.Client('localhost')
        pass
