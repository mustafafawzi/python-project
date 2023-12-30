import pandas as pd
import openpyxl

class ReportGenerator:
    """
    Generates reports in CSV and Excel formats.
    """

    @staticmethod
    def generate_csv(data, filename):
        """
        Generates a CSV report.

        Args:
            data (list of lists): The data to write to the CSV file.
            filename (str): The name of the CSV file to create.
        """

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

    @staticmethod
    def generate_excel(data, filename):
        """
        Generates an Excel report using OpenPyXL, with error handling and potential enhancements.

        Args:
            data (list of lists): The data to write to the Excel file.
            filename (str): The name of the Excel file to create.
        """

        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active

            # Write data to cells
            for row_index, row in enumerate(data):
                for col_index, value in enumerate(row):
                    sheet.cell(row=row_index + 1, column=col_index + 1, value=value)

            # Potential enhancements:
            # - Apply formatting to cells, rows, and columns
            # - Add charts and visualizations using OpenPyXL's Chart module
            # - Implement conditional formatting using conditional_formatting module

            workbook.save(filename)  # Ensure filename has '.xlsx' extension

        except Exception as e:
            print(f"An error occurred while generating Excel file: {e}")
