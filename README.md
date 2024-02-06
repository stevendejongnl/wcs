# Web Components Scan

WCS is a Python application that scans HTML files within a specified directory based on the `@custom-elements-manifest/analyzer` npm package.
This npm packages generates a `custom-elements.json` file containing information about custom HTML tags.
With this file we can scan html files for implementations.

# Installation
Clone this repository to your local machine.

# Install the required Python dependencies using pip:
```bash
pip install -r requirements.txt
```

# Usage
Run the analyzer script with the following command:
```bash
python main.py --scan-path <path_to_directory> --manifest-path <path_to_manifest>
```

Replace `<path_to_directory>` with the path to the directory containing your HTML files.
And `<path_to_manifest>` with the path to your `custom-elements.json`.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
