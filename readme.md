# TikZ Diagram Generation using LLMs

This project aims to fine-tune a Large Language Model (LLM) to generate accurate TikZ code for mathematical and physics diagrams. The model will be trained to understand natural language descriptions of physics concepts and generate corresponding TikZ diagrams.

## Project Structure

```
project/
├── diagram_dataset/
│   ├── TikZ_examples/           # Source TikZ examples
│   │   ├── work_and_energy.tex
│   │   ├── tension_in_ropes.tex
│   │   ├── pulley_mass_systems.tex
│   │   ├── springs_and_masses.tex
│   │   ├── normal_force.tex
│   │   └── friction.tex
│   ├── LaTeX_manuals/          # Reference documentation
│   ├── processed/              # Processed dataset (generated)
│   │   ├── *.md               # Human-readable markdown files
│   │   └── *_metadata.json    # Machine learning ready JSON files
│   └── dataExtraction.py      # Data processing script
└── readme.md
```

## Current Status

### Completed
1. **Data Collection**
   - Gathered TikZ examples for various physics concepts
   - Organized examples by physics domains (mechanics, energy, etc.)
   - Included reference LaTeX manuals

2. **Data Processing Pipeline**
   - Created `dataExtraction.py` script to:
     - Extract TikZ code from LaTeX files
     - Generate structured markdown documentation
     - Create machine learning ready JSON datasets
     - Extract metadata (complexity, concepts, libraries)
     - Identify custom styles and commands

### In Progress
1. **Dataset Enhancement**
   - [ ] Add more diverse physics examples
   - [ ] Include mathematical diagrams
   - [ ] Create synthetic examples through parameter variation
   - [ ] Add more detailed descriptions and annotations

2. **Data Quality**
   - [ ] Validate TikZ code compilation
   - [ ] Review and improve descriptions
   - [ ] Standardize diagram complexity ratings
   - [ ] Expand concept taxonomy

## Pipeline for LLM Fine-tuning

### Phase 1: Data Preparation (Current)
1. **Data Collection and Organization** ✅
   - Gather TikZ examples
   - Organize by physics domains
   - Include reference documentation

2. **Data Processing** ✅
   - Extract TikZ code
   - Generate structured datasets
   - Create metadata

3. **Data Enhancement** (Next Steps)
   - [ ] Create synthetic examples
   - [ ] Add more detailed descriptions
   - [ ] Validate and clean dataset
   - [ ] Create train/validation/test splits

### Phase 2: Model Preparation
1. **Base Model Selection**
   - [ ] Evaluate available LLMs
   - [ ] Choose appropriate model size
   - [ ] Consider computational requirements

2. **Training Setup**
   - [ ] Define training objectives
   - [ ] Create evaluation metrics
   - [ ] Set up training infrastructure
   - [ ] Prepare training scripts

### Phase 3: Training and Evaluation
1. **Model Training**
   - [ ] Implement fine-tuning pipeline
   - [ ] Train on processed dataset
   - [ ] Monitor training metrics
   - [ ] Implement early stopping

2. **Evaluation**
   - [ ] Test on validation set
   - [ ] Evaluate diagram accuracy
   - [ ] Check mathematical correctness
   - [ ] Assess code quality

### Phase 4: Deployment and Monitoring
1. **Model Deployment**
   - [ ] Create API for diagram generation
   - [ ] Implement input validation
   - [ ] Set up error handling
   - [ ] Create documentation

2. **Monitoring and Updates**
   - [ ] Track usage metrics
   - [ ] Collect user feedback
   - [ ] Plan model updates
   - [ ] Maintain dataset

## Getting Started

### Prerequisites
- Python 3.8+
- PyMuPDF (fitz)
- LaTeX distribution (for validation)

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install PyMuPDF
   ```
3. Run the data extraction script:
   ```bash
   python diagram_dataset/dataExtraction.py
   ```

### Usage
The data extraction script will:
1. Process all TikZ examples in `diagram_dataset/TikZ_examples/`
2. Generate markdown documentation in `diagram_dataset/processed/`
3. Create JSON metadata files for machine learning

## Next Steps

### Immediate Tasks
1. **Dataset Enhancement**
   - Add more physics examples
   - Create synthetic variations
   - Improve descriptions
   - Validate TikZ code

2. **Model Preparation**
   - Research suitable base models
   - Define training objectives
   - Set up evaluation metrics

### Future Work
1. **Model Development**
   - Implement fine-tuning pipeline
   - Train and evaluate model
   - Optimize performance

2. **Deployment**
   - Create API
   - Set up monitoring
   - Plan updates