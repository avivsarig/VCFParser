# VCF File Filter and Parser
This project consists of a VCF file parser and filter. It handles compressed VCF files stored in Amazon S3, parses the files to extract relevant information, applies specific filtering criteria, and outputs the filtered results into separate files.

## How to Use
### Prerequisites
Python 3.7 or later
The following Python libraries: boto3, requests, and typer
Two environment variables set: FILE_PATH and API_URI

## Configuration
This script uses environment variables for configuration. The following environment variables are used:
FILE_PATH: The S3 file path of the VCF file you want to process. Example: "s3://resources.genoox.com/homeAssingment/demo_vcf_multisample.vcf.gz"
API_URI: The URI of the API you'll use to fetch gene details. Example: "https://test.genoox.com/api/fetch_variant_details"

## Running the Application
Clone the repository:
```
git clone <repository_url>
```
Navigate into the project directory:
```
cd <project_directory>
```
Install the required Python packages:
```
pip install -r requirements.txt
```
Run the application:
```
python main.py process --limit 5
```

### Application Commands
The application supports the following commands:

```Process```: This command downloads a compressed VCF file, parses it, applies filters, and outputs the results into separate files.
```
python main.py process --limit <limit> --start <start> --end <end> --minDP <minDP> --deNovo <deNovo>
```
#### Arguments:
```limit```: Maximum number of variants to be processed.

```start```: The start position for filtering. Defaults to 0.

```end```: The end position for filtering. Defaults to -1, which means no end limit.

```minDP```: Minimum depth to filter by. Defaults to -1, which means no depth limit.

```deNovo```: Boolean flag for de novo mutations. If True, only de novo mutations are considered.

#### Utility Commands
```Clear Cache```: This command resets the contents of the Gene Cache.
```
python main.py clear_cache
```

```Clear Output```: This command resets the contents of the output folder.
```
python main.py clear_output
```

## Code Structure
The main components of the application are:

main.py: The entry point of the application. It handles the user commands.

utils: This directory contains various utility functions, including S3 file retrieval, API calls, and data classification.

parse_functions: This directory contains functions for parsing and filtering the VCF data.


## Please note
This application makes use of the Gene API for gene retrieval, and stores the results in a local cache for faster future retrievals. The cache is stored in a json file and can be reset using the 'clear_cache' command.
