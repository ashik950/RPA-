# Azure Form Recognizer PDF Extraction Script  

## 📌 Overview  
This Python script extracts specific fields (`OurRef` and `PermitNumber`) from PDF documents using **Azure Form Recognizer**. It processes PDFs in a given directory and outputs the extracted data in JSON format.  

## 🚀 Features  
- **Uses Azure Form Recognizer** to extract text from scanned PDFs.  
- **Batch Processing**: Reads multiple PDFs from a specified directory.  
- **Custom Model Support**: Uses a trained model (`test11`) for document analysis.  
- **JSON Output**: Extracted values are structured in JSON format for easy integration.  

## 🛠️ Installation  

### **1. Install Dependencies**  
Ensure you have Python installed, then install the required libraries:  
```bash
pip install azure-ai-formrecognizer azure-core
