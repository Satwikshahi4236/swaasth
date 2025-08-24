from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models so that metadata is populated for create_all
from .models.user import User  # noqa: F401
from .models.medicine import Medicine  # noqa: F401
from .models.reminder import Reminder  # noqa: F401
from .models.message import Message  # noqa: F401
from .models.device import Device  # noqa: F401