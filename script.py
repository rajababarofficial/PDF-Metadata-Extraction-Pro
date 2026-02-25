# ==========================================================
# SOFTWARE: PDF Metadata Extraction Pro
# DEVELOPED BY: RAJA BABAR
# WEBSITE: https://rajababar.com
# REPOSITORY: https://github.com/YourUsername/PDF-Metadata-Extraction-Pro
# LICENSE: MIT License
# ==========================================================
# Description: This engine extracts structured metadata 
# with high precision and customizable export formats.
# ==========================================================

import os
import csv
import customtkinter as ctk
from tkinter import filedialog, messagebox
import PyPDF2
from datetime import datetime

# UI Theme Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class PDFExtractorPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF Metadata Engine Pro")
        self.geometry("700x450")
        
        # Grid layout for professional structure
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # Branding only at the bottom now
        self.credits = ctk.CTkLabel(self.sidebar, text="rajababar.com", font=("Arial", 12, "bold"), text_color="#1f6aa5")
        self.credits.pack(side="bottom", pady=30)

        # --- Main Panel ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")

        self.header = ctk.CTkLabel(self.main_frame, text="PDF Metadata Extractor", font=("Arial", 28, "bold"))
        self.header.pack(pady=(0, 10), anchor="w")
        
        self.sub_header = ctk.CTkLabel(self.main_frame, text="Batch process PDFs to CSV with optimized sequencing.", text_color="gray")
        self.sub_header.pack(pady=(0, 30), anchor="w")

        # Select Folder Button
        self.btn_folder = ctk.CTkButton(self.main_frame, text="📁 Choose Source Folder", command=self.browse_folder, height=45, fg_color="#333", hover_color="#444")
        self.btn_folder.pack(fill="x", pady=5)
        self.lbl_folder = ctk.CTkLabel(self.main_frame, text="No folder selected", text_color="gray", font=("Arial", 11))
        self.lbl_folder.pack(pady=(0, 15))

        # Export Path Button
        self.btn_save = ctk.CTkButton(self.main_frame, text="💾 Set Export Location (Optional)", command=self.set_save_location, height=45, fg_color="#333", hover_color="#444")
        self.btn_save.pack(fill="x", pady=5)
        self.lbl_save = ctk.CTkLabel(self.main_frame, text="Default: metadata_export.csv", text_color="gray", font=("Arial", 11))
        self.lbl_save.pack(pady=(0, 30))

        # Final Action Button
        self.btn_run = ctk.CTkButton(self.main_frame, text="RUN EXTRACTION", command=self.process_files, height=55, font=("Arial", 16, "bold"), fg_color="#1f6aa5", hover_color="#144870")
        self.btn_run.pack(fill="x")

        self.selected_folder = ""
        self.save_path = ""

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            self.lbl_folder.configure(text=folder, text_color="#1f6aa5")

    def set_save_location(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if path:
            self.save_path = path
            self.lbl_save.configure(text=path, text_color="#1f6aa5")

    def process_files(self):
        if not self.selected_folder:
            messagebox.showwarning("Warning", "Pehle PDF folder select karein!")
            return

        try:
            pdf_files = [f for f in os.listdir(self.selected_folder) if f.lower().endswith('.pdf')]
            if not pdf_files:
                messagebox.showerror("Empty", "Folder mein koi PDF nahi mili!")
                return

            all_data = []
            custom_keys = set()
            system_keys = set(['Size_MB', 'Producer', 'Creator', 'CreationDate', 'ModDate'])
            primary_keys = ['File_Name', 'Title', 'Author', 'Pages']

            for pdf in pdf_files:
                full_path = os.path.join(self.selected_folder, pdf)
                info = {k: '' for k in primary_keys + list(system_keys)}
                info['File_Name'] = pdf
                info['Size_MB'] = round(os.path.getsize(full_path)/(1024*1024), 2)
                
                try:
                    with open(full_path, 'rb') as f:
                        reader = PyPDF2.PdfReader(f)
                        info['Pages'] = len(reader.pages)
                        meta = reader.metadata
                        if meta:
                            for k, v in meta.items():
                                clean_k = k.replace('/', '').strip()
                                # Mapping
                                if clean_k.lower() == 'title': info['Title'] = str(v)
                                elif clean_k.lower() == 'author': info['Author'] = str(v)
                                elif clean_k in system_keys: info[clean_k] = str(v)
                                elif clean_k not in primary_keys:
                                    info[clean_k] = str(v)
                                    custom_keys.add(clean_k)
                    all_data.append(info)
                except: continue

            # Final Column Sequence logic
            final_columns = primary_keys + sorted(list(custom_keys)) + sorted(list(system_keys))

            # Default Save Path (Simple name)
            if not self.save_path:
                self.save_path = os.path.join(os.getcwd(), "metadata_export.csv")

            # --- Export Logic ---
            with open(self.save_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=final_columns, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(all_data)

            messagebox.showinfo("Success", f"Extraction Complete!\n\nFile saved at:\n{self.save_path}")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = PDFExtractorPro()
    app.mainloop()