from prometheus_client import Counter
from prometheus_client import Histogram


REQUEST_COUNTER = Counter(
    "inference_requests_total",
    "Total inference requests"
)

INFERENCE_LATENCY = Histogram(
    "inference_latency_seconds",
    "Inference latency"
)
