import logging

logging.basicConfig(
    format='[%(asctime)s - %(filename)s - %(levelname)s] %(message)s',
    level=logging.DEBUG
)

from . import gov
from . import graph
