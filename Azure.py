import glob
import os
import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from pathlib import Path

# Azure Form Recognizer credentials and endpoint
endpoint = "https://ij-clouddemo-form-recognizer.cognitiveservices.azure.com/"
key = "7f7d90a8920a4fb1a3892e4e5e16d1c6"

# Model ID for document analysis
model_id = "test11"

# Directory containing the PDF files
pdf_dir = r"F:\pdf extraction"

# Create a Form Recognizer client
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Get a list of PDF files in the directory
pdf_files = glob.glob(os.path.join(pdf_dir, "*.pdf"))

# Process each PDF file
for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as file:
        poller = document_analysis_client.begin_analyze_document(model_id, file.read())
        result = poller.result()

        our_ref_values = []
        permit_numbers = []

        for document in result.documents:
            fields = document.fields
            our_ref_value = fields.get("OurRef", {}).value
            permit_number = fields.get("permit_number", {}).value

            our_ref_values.append(our_ref_value)
            permit_numbers.append(permit_number)

        # Create a dictionary to hold the values
        output = {
            "OurRef": our_ref_values,
            "PermitNumber": permit_numbers
        }

        # Convert the dictionary to JSON format
        output_json = json.dumps(output, indent=4)

        # Print the JSON value
        print("Reading file:", pdf_file)
        print(output_json)