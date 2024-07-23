import typing as tp
import heapq

def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    heap = [(next(stream).rstrip(b"\n"), stream) for stream in input_streams if (line := next(stream)) != b""]
    heapq.heapify(heap)

    
    while heap:
        line, stream = heapq.heappop(heap)
        output_stream.write(line + b"\n")

        
        if (line := next(stream, b"")) != b"":
            heapq.heappush(heap, (line, stream))
