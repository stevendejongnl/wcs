import argparse
import json

from WebComponentsScan.web_components_scan import WebComponentsScan


def main() -> None:
    parser = argparse.ArgumentParser(description='Web Components Scanner')
    parser.add_argument(
        '--scan-path', type=str, default='./',
        help='Path to the directory to scan for HTML files'
    )
    parser.add_argument(
        '--manifest-path', type=str, default='./custom-elements.json',
        help='Path to the custom elements manifest file'
    )
    args = parser.parse_args()

    wcs = WebComponentsScan()
    results = wcs.scan_html(path=args.scan_path, manifest=args.manifest_path)

    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
