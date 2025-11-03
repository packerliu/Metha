#!/usr/bin/env python3
"""
Lightweight script inspired by metha.py::run_single_test

This script only initializes a GNS3 project from files and prints a success
message. It purposefully avoids importing or instantiating any of the
`Systems.*` classes to prevent heavy side-effects at import time.

Usage examples:
  python3 run_single_gns3.py -p example-tests/tests-new/test0/
  python3 run_single_gns3.py -p /absolute/path/to/project -s nv

The `--system` argument is accepted for compatibility with metha's CLI, but
it is not used by this script (no comparisons are performed).
"""
import argparse
import time
from GNS3 import gns3_interface


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Initialize a GNS3 project from files and exit (no comparisons)."
    )
    parser.add_argument('-p', '--path', required=True,
                        help='Path to the directory containing GNS3 project files')
    parser.add_argument('-s', '--system', choices=['batfish', 'cbgp', 'nv'],
                        help='(optional) system name for compatibility; not used')
    parser.add_argument('--wait', type=int, default=0,
                        help='Number of seconds to wait before exiting (keeps GNS3 project running during this time)')
    parser.add_argument('--attach-debug', action='store_true',
                        help='If set, listen on 0.0.0.0:5678 and wait for a debugpy client to attach before continuing')

    args = parser.parse_args(argv)

    # If requested, allow attaching a remote debugger before proceeding.
    if getattr(args, 'attach_debug', False):
        try:
            import debugpy
            debugpy.listen(("0.0.0.0", 5678))
            print("Waiting for client to attach...")
            debugpy.wait_for_client()
        except Exception as e:
            print(f"debugpy attach failed or not available: {e}")

    try:
        # This mirrors the call in metha.run_single_test
        gp, adj = gns3_interface.init_gns_from_files(args.path)
    except Exception as e:
        print(f"Error initializing GNS3 project from '{args.path}': {e}")
        raise

    # Minimal success output; keep it simple and non-destructive.
    node_count = len(getattr(gp, 'nodes', {}))
    print(f"success! initialized GNS3 project at '{args.path}' (nodes: {node_count})")

    # Optionally wait to keep the project running for interactive debugging / access.
    if args.wait and args.wait > 0:
        print(f"Waiting {args.wait} seconds before exiting (project will remain available)...")
        try:
            time.sleep(args.wait)
        except KeyboardInterrupt:
            print("Interrupted by user; continuing to cleanup/exit")


if __name__ == '__main__':
    # Allow attaching a remote debugger before the script proceeds (same
    # behaviour as in `metha.py`). This will block until a debug client
    # attaches to port 5678.
    try:
        import debugpy
        debugpy.listen(("0.0.0.0", 5678))
        print("Waiting for client to attach...")
        debugpy.wait_for_client()
    except Exception:
        # If debugpy is not installed or listening fails, continue without
        # blocking so the script still runs in non-debug environments.
        pass

    main()
