# VCF File Filter and Parser

This project consists of a VCF file parser and filter. It handles compressed VCF files stored in Amazon S3, parses the files to extract relevant information, applies specific filtering criteria, and outputs the filtered results into separate files.

## How to Use

### Prerequisites

- Python 3.7 or later
- An AWS account with permissions to access S3
- The following Python libraries: boto3, requests, and typer

### Running the Application

1. Clone the repository:
   ```
   git clone <repository_url>
   ```
2. Navigate into the project directory:
   ```
   cd <project_directory>
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python main.py
   ```

### Application Commands

The application supports the following commands:

1. **Filtering**: This command downloads a compressed VCF file, parses it, applies filters, and outputs the results into separate files.

   ```
   python main.py filter --limit <limit> --start <start> --end <end> --minDP <minDP> --deNovo <deNovo>
   ```

   Arguments:

   - limit: Maximum number of variants to be processed.
   - start: The start position for filtering. Defaults to 0.
   - end: The end position for filtering. Defaults to -1, which means no end limit.
   - minDP: Minimum depth to filter by. Defaults to -1, which means no depth limit.
   - deNovo: Boolean flag for de novo mutations. If True, only de novo mutations are considered.

2. **Clear Cache**: This command resets the contents of the Gene Cache.
   ```
   python main.py clear_cache
   ```
3. **Clear Output**: This command resets the contents of the output folder.
   ```
   python main.py clear_output
   ```

## Code Structure

The main components of the application are:

- `main.py`: The entry point of the application. It handles the user commands.
- `utils`: This directory contains various utility functions, including S3 file retrieval, API calls, and data classification.
- `parse_functions`: This directory contains functions for parsing and filtering the VCF data.

Please note that this application makes use of the Gene API for gene retrieval, and stores the results in a local cache for faster future retrievals. The cache is stored in a `json` file and can be reset using the 'clear_cache' command.

## Important

Please remember that this application requires appropriate AWS credentials set up in your environment to access the S3 service.
