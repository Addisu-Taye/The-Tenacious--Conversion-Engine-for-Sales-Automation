import json
from statistics import median

# Replace these with real values from your trace metadata if you have them
latencies = [1100, 1250, 980, 1320, 1410, 1190, 1075, 1500, 1210, 1175]

latencies_sorted = sorted(latencies)

def percentile(values, p):
    if not values:
        return None
    k = (len(values) - 1) * p
    f = int(k)
    c = min(f + 1, len(values) - 1)
    if f == c:
        return values[f]
    d0 = values[f] * (c - k)
    d1 = values[c] * (k - f)
    return d0 + d1

result = {
    "sample_size": len(latencies),
    "p50_latency_ms": median(latencies),
    "p95_latency_ms": percentile(latencies_sorted, 0.95),
    "note": "Prototype-only estimate; replace with 20+ real trace-derived interactions for rubric compliance."
}

print(json.dumps(result, indent=2))