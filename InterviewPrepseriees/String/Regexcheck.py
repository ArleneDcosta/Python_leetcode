import csv
import re
import os
import pandas as pd
import openpyxl

class TextReplacementRules:
    def _init_(self, file_path):
        self.file_path = file_path
        self.pattern_dict = self._load_patterns()

    def _load_patterns(self):
        pattern_dict = {}
        with open(self.file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                raw_from = row.get('From', '').strip()
                if self.looks_like_regex(raw_from):
                    pattern = raw_from  # leave it as-is
                else:
                    pattern = re.escape(raw_from)
                raw_to = row.get('To', '').strip()

                pattern_dict[pattern] = raw_to

        return pattern_dict

    def get_patterns(self):
        return self.pattern_dict
    
    def looks_like_regex(self, text):
        regex_chars = set("{}+*?|\\^$")
        return any(char in regex_chars for char in text)
    
    def apply_substitutions(self, text):
        for pattern, replacement in self.pattern_dict.items():
            if re.search(pattern, text):
                print(f"Matched pattern: {pattern} -> {replacement}")
                text = re.sub(pattern, replacement, text)
        return text
    
    def process_excel(self, excel_path, output_path):
        # Load all sheets into a dictionary of DataFrames
        xl = pd.read_excel(excel_path, sheet_name=None)

        updated_sheets = {}

        for sheet_name, df in xl.items():
            print(f"Processing sheet: {sheet_name}")
            if 'FROM' in df.columns and 'TO' in df.columns:
                df['FROM'] = df['FROM'].astype(str).apply(self.apply_substitutions)
                df['TO'] = df['TO'].astype(str).apply(self.apply_substitutions)

            else:
                print(f"Skipping sheet {sheet_name}: Missing FROM/TO columns")
            updated_sheets[sheet_name] = df
            
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            for sheet_name, df in updated_sheets.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)