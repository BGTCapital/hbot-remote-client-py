from typing import Any, List, Optional, Tuple
from commlib.msg import PubSubMessage, RPCMessage, HeartbeatMessage


class BROKER_STATUS_CODE:
    ERROR: int = 400
    SUCCESS: int = 200


class NotifyMessage(PubSubMessage):
    seq: Optional[int] = 0
    timestamp: Optional[int] = -1
    msg: Optional[str] = ''


class EventMessage(PubSubMessage):
    timestamp: Optional[int] = -1
    type: Optional[str] = 'Unknown'
    data: Optional[dict] = {}


class LogMessage(PubSubMessage):
    timestamp: float = 0.0
    msg: str = ''
    level_no: int = 0
    level_name: str = ''
    logger_name: str = ''


class StartCommandMessage(RPCMessage):
    class Request(RPCMessage.Request):
        log_level: Optional[str] = None
        script: Optional[str] = None
        is_quickstart: Optional[bool] = False
        async_backend: Optional[bool] = False

    class Response(RPCMessage.Response):
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''


class StopCommandMessage(RPCMessage):
    class Request(RPCMessage.Request):
        skip_order_cancellation: Optional[bool] = False
        async_backend: Optional[bool] = False

    class Response(RPCMessage.Response):
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''


class ConfigCommandMessage(RPCMessage):
    class Request(RPCMessage.Request):
        params: Optional[List[Tuple[str, Any]]] = []

    class Response(RPCMessage.Response):
        changes: Optional[List[Tuple[str, Any]]] = []
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''


class CommandShortcutMessage(RPCMessage):
    class Request(RPCMessage.Request):
        params: Optional[List[List[Any]]] = []

    class Response(RPCMessage.Response):
        success: Optional[List[bool]] = []
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''


class ImportCommandMessage(RPCMessage):
    class Request(RPCMessage.Request):
        strategy: str

    class Response(RPCMessage.Response):
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''


class StatusCommandMessage(RPCMessage):
    class Request(RPCMessage.Request):
        async_backend: Optional[bool] = True

    class Response(RPCMessage.Response):
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''
        data: Optional[Any] = ''


class HistoryCommandMessage(RPCMessage):
    class Request(RPCMessage.Request):
        days: Optional[float] = 0
        verbose: Optional[bool] = False
        precision: Optional[int] = None
        async_backend: Optional[bool] = True

    class Response(RPCMessage.Response):
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''
        trades: Optional[List[Any]] = []


class BalanceLimitCommandMessage(RPCMessage):
    class Request(RPCMessage.Request):
        exchange: str
        asset: str
        amount: float

    class Response(RPCMessage.Response):
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''
        data: Optional[str] = ''


class BalancePaperCommandMessage(RPCMessage):
    class Request(RPCMessage.Request):
        asset: str
        amount: float

    class Response(RPCMessage.Response):
        status: Optional[int] = BROKER_STATUS_CODE.SUCCESS
        msg: Optional[str] = ''
        data: Optional[str] = ''
