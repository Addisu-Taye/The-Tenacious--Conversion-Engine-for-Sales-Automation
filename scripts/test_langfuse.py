import time
from agent.observability.langfuse_client import langfuse

start = time.time()

with langfuse.start_as_current_observation(
    as_type="span",
    name="day0-test",
    input={"step": "langfuse_setup"},
) as root:
    time.sleep(1)
    latency_ms = int((time.time() - start) * 1000)
    root.update(
        output={"status": "success"},
        metadata={
            "latency_ms": latency_ms,
            "channel": "system",
            "env": "dev",
            "component": "langfuse_smoke_test",
        },
    )

print("Langfuse test observation sent")