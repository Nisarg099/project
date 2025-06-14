import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown("/Users/system/Desktop/NPTEL_Internship/project/diagram_dataset/LaTeX_manuals/pgfmanual_parse.pdf")
pathlib.Path("/Users/system/Desktop/NPTEL_Internship/project/diagram_dataset/output.md").write_bytes(md_text.encode())
