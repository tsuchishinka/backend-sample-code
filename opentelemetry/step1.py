import time

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

from opentelemetry import trace

resource = Resource.create({"service.name": "python-sample"})

provider = TracerProvider(resource=resource)

exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")

provider.add_span_processor(SimpleSpanProcessor(exporter))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)


def fetch_data():
    with tracer.start_as_current_span("fetch_data") as span:
        span.set_attribute("sample.item_count", 3)
        time.sleep(0.6)
        return ["apple", "banana", "orange"]


def main():
    with tracer.start_as_current_span("main"):
        items = fetch_data()
        print(items)


if __name__ == "__main__":
    try:
        main()
    finally:
        provider.shutdown()
