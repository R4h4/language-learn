"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ


def max_workers():
    """
    Following:
    https://stackoverflow.com/questions/15979428/what-is-the-appropriate-number-of-gunicorn-workers-for-each-amazon-instance-type
    """
    return cpu_count() * 2 + 1


bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 1000
# worker_class = 'gevent'
# threads = max_workers()
