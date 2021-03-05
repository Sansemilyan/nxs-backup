import general_function


class Job(object):
    """
    The general Job class
    """

    def __init__(self, job_data):
        is_prams_read, job_name, options = general_function.get_job_parameters(job_data)
        if not is_prams_read:
            raise general_function.MyError('Failed to get job parameter.')

        self.options = options
        self.name = job_name
        super(Job, self).__init__()

    def do_backup(self):
        raise NotImplementedError


class JobsBlock:
    start_message: str
    finish_message: str
    jobs: dict

    def __init__(self, block_name, jobs):
        self.start_message = f"Starting {block_name} backup block.\n"
        self.finish_message = f"Finishing {block_name} backup block.\n"
        self.jobs = jobs
