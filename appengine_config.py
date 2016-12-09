import os
from google.appengine.ext import vendor


DEBUG = (
    os.environ.get('SERVER_SOFTWARE', 'Unknown') == 'Unknown' or
    os.environ.get('SERVER_SOFTWARE', 'Unknown').startswith('Dev')
)
# vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'libs'))


def namespace_manager_default_namespace_for_request():
    """
    used for setting the global namespace for all queries against the datastore
    :return: string to use for namespace
    """
    return None if DEBUG else 'v1'
