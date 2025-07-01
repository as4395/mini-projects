import subprocess
import argparse
import trace

def run_with_tracer(file_path):
    tracer = trace.Trace(
        ignoredirs=[sys.prefix, sys.exec_prefix],
        trace=False,
        count=True
    )
    print("[*] Executing file with tracing enabled...")
    tracer.run(f'exec(open("{file_path}").read())')

if __name__ == "__main__":
    import sys
    parser = argparse.ArgumentParser(description="Dynamic Code Analyzer")
    parser.add_argument("--file", required=True, help="Path to Python file to run")
    args = parser.parse_args()

    run_with_tracer(args.file)
