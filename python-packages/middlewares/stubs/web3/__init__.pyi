from typing import Dict, Optional, Union

from web3.utils import datatypes
from web3.providers.base import BaseProvider

class Web3:
    class HTTPProvider(BaseProvider): ...
    def __init__(self, provider: BaseProvider) -> None: ...
