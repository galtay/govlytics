import logging

logging.basicConfig(
    format='[%(asctime)s - %(filename)s - %(levelname)s] %(message)s',
    level=logging.INFO
)

from . import gov
from . import graph

gov.data_utils.create_govlytics_dirs()
