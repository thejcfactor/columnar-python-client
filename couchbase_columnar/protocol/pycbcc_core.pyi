#  Copyright 2016-2024. Couchbase, Inc.
#  All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from enum import IntEnum, auto
from typing import (Any,
                    Dict,
                    Optional,
                    Union)

from couchbase_columnar.common.core.query import QueryMetadataCore
from couchbase_columnar.protocol.core import PyCapsuleType
from couchbase_columnar.protocol.exceptions import CoreColumnarError

CXXCBC_METADATA: str

class core_errors(IntEnum):
    VALUE = 1
    RUNTIME = 2
    INTERNAL_SDK = 3

class core_error:
    @classmethod
    def __init__(cls, *args: object, **kwargs: object) -> None: ...
    def error_details(self) -> Optional[Dict[str, Any]]: ...

class pycbcc_logger:
    @classmethod
    def __init__(cls, *args: object, **kwargs: object) -> None: ...
    def configure_logging_sink(self, *args: object, **kwargs: object) -> None: ...
    def create_console_logger(self, *args: object, **kwargs: object) -> None: ...
    def enable_protocol_logger(self, *args: object, **kwargs: object) -> None: ...

class result:
    raw_result: Dict[str, Any]
    @classmethod
    def __init__(cls, *args: object, **kwargs: object) -> None: ...
    def err(self, *args: object, **kwargs: object) -> Optional[int]: ...
    def err_category(self, *args: object, **kwargs: object) -> Optional[str]: ...
    def get(self, *args: object, **kwargs: object) -> Any: ...
    def strerror(self, *args: object, **kwargs: object) -> Optional[str]: ...

class columnar_query_iterator:
    @classmethod
    def __init__(cls, *args: object, **kwargs: object) -> None: ...
    def cancel(self) -> None: ...
    def wait_for_core_query_result(self) -> Union[bool, CoreColumnarError]: ...
    def metadata(self) -> Optional[QueryMetadataCore]: ...
    # def is_cancelled(self, *args: object, **kwargs: object) -> bool: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...

def columnar_query(*args: object, **kwargs: object) -> columnar_query_iterator: ...
def close_connection(*args: object, **kwargs: object) -> bool: ...
def cluster_info(*args: object, **kwargs: object) -> result: ...
def create_connection(*args: object, **kwargs: object) -> PyCapsuleType: ...
def get_connection_info(*args: object, **kwargs: object) -> result: ...
def _test_exception_builder(error_type: int,
                            build_cpp_core_exception: Optional[bool]=False,
                            set_inner_cause: Optional[bool]=False) -> CoreColumnarError: ...
