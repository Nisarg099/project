import os
import re
import json
import fitz  # PyMuPDF
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class TikZExtractor:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Common TikZ libraries and styles
        self.common_libraries = {
            'angles', 'quotes', 'patterns', 'snakes', 'calc',
            'arrows', 'shapes', 'positioning', 'decorations'
        }
        
        # Physics categories mapping
        self.category_mapping = {
            'work_and_energy': 'energy',
            'tension_in_ropes': 'mechanics',
            'pulley_mass_systems': 'mechanics',
            'springs_and_masses': 'mechanics',
            'normal_force': 'mechanics',
            'friction': 'mechanics'
        }

    def extract_tikz_code(self, file_path: Path) -> List[Dict]:
        """Extract TikZ code blocks from a LaTeX file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all tikzpicture environments
        tikz_blocks = re.finditer(
            r'\\begin{tikzpicture}(.*?)\\end{tikzpicture}',
            content,
            re.DOTALL
        )

        # Extract required libraries
        libraries = set()
        lib_pattern = r'\\usetikzlibrary{([^}]*)}'
        for match in re.finditer(lib_pattern, content):
            libraries.update(match.group(1).split(','))

        # Extract custom styles and commands
        styles = []
        style_pattern = r'\\tikzstyle{([^}]*)}=([^;]*);'
        for match in re.finditer(style_pattern, content):
            styles.append({
                'name': match.group(1).strip(),
                'definition': match.group(2).strip()
            })

        # Process each TikZ block
        diagrams = []
        for i, block in enumerate(tikz_blocks, 1):
            tikz_code = block.group(0)
            
            # Try to extract a description from comments
            description = self._extract_description(content, block.start())
            
            # Determine complexity based on code length and features
            complexity = self._determine_complexity(tikz_code)
            
            # Extract mathematical concepts
            concepts = self._extract_concepts(tikz_code)
            
            diagrams.append({
                'id': f"{file_path.stem}_{i}",
                'description': description,
                'tikz_code': tikz_code,
                'metadata': {
                    'category': self.category_mapping.get(file_path.stem, 'general'),
                    'complexity': complexity,
                    'required_libraries': list(libraries),
                    'mathematical_concepts': concepts,
                    'custom_styles': styles
                }
            })

        return diagrams

    def _extract_description(self, content: str, block_start: int) -> str:
        """Extract description from comments before the TikZ block."""
        # Look for comments in the 10 lines before the block
        lines = content[:block_start].split('\n')[-10:]
        comments = []
        for line in reversed(lines):
            if line.strip().startswith('%'):
                comments.append(line.strip('% ').strip())
            else:
                break
        return ' '.join(reversed(comments)) if comments else "Physics diagram"

    def _determine_complexity(self, tikz_code: str) -> str:
        """Determine the complexity of a TikZ diagram."""
        # Simple heuristics for complexity
        lines = tikz_code.count('\n')
        nodes = tikz_code.count('\\node')
        paths = tikz_code.count('\\path')
        draws = tikz_code.count('\\draw')
        
        if lines < 20 and nodes + paths + draws < 10:
            return 'beginner'
        elif lines < 50 and nodes + paths + draws < 25:
            return 'intermediate'
        else:
            return 'advanced'

    def _extract_concepts(self, tikz_code: str) -> List[str]:
        """Extract mathematical/physics concepts from the TikZ code."""
        concepts = set()
        
        # Common physics concepts to look for
        physics_terms = {
            'force', 'mass', 'velocity', 'acceleration', 'tension',
            'friction', 'spring', 'pulley', 'energy', 'work',
            'momentum', 'gravity', 'normal', 'weight'
        }
        
        # Look for these terms in the code
        for term in physics_terms:
            if term in tikz_code.lower():
                concepts.add(term)
        
        return list(concepts)

    def process_file(self, file_path: Path) -> None:
        """Process a single LaTeX file and save its diagrams."""
        try:
            diagrams = self.extract_tikz_code(file_path)
            
            # Create markdown output
            md_content = f"# {file_path.stem.replace('_', ' ').title()}\n\n"
            
            for diagram in diagrams:
                md_content += f"## Diagram {diagram['id']}\n\n"
                md_content += f"**Description:** {diagram['description']}\n\n"
                md_content += "**Metadata:**\n"
                md_content += f"- Category: {diagram['metadata']['category']}\n"
                md_content += f"- Complexity: {diagram['metadata']['complexity']}\n"
                md_content += f"- Required Libraries: {', '.join(diagram['metadata']['required_libraries'])}\n"
                md_content += f"- Mathematical Concepts: {', '.join(diagram['metadata']['mathematical_concepts'])}\n\n"
                
                if diagram['metadata']['custom_styles']:
                    md_content += "**Custom Styles:**\n"
                    for style in diagram['metadata']['custom_styles']:
                        md_content += f"- {style['name']}: `{style['definition']}`\n"
                    md_content += "\n"
                
                md_content += "**TikZ Code:**\n```latex\n"
                md_content += diagram['tikz_code']
                md_content += "\n```\n\n"
                md_content += "---\n\n"
            
            # Save markdown file
            output_file = self.output_dir / f"{file_path.stem}.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
            # Save JSON metadata
            json_file = self.output_dir / f"{file_path.stem}_metadata.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(diagrams, f, indent=2)
                
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

    def process_all_files(self) -> None:
        """Process all LaTeX files in the input directory."""
        for file_path in self.input_dir.glob('*.tex'):
            print(f"Processing {file_path.name}...")
            self.process_file(file_path)

def main():
    # Set up directories
    input_dir = Path('diagram_dataset/TikZ_examples')
    output_dir = Path('diagram_dataset/processed')
    
    # Create and run extractor
    extractor = TikZExtractor(input_dir, output_dir)
    extractor.process_all_files()
    
    print("Processing complete! Check the 'processed' directory for results.")

if __name__ == "__main__":
    main()
