# agent/observability/tracer.py
import time
from .langfuse_client import langfuse

def start_trace(name, metadata=None):
    return langfuse.trace(
        name=name,
        metadata=metadata or {},
        input={}
    )

def end_trace(trace, output, metadata=None):
    trace.update(
        output=output,
        metadata=metadata or {}
    )