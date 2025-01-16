# Multimodal-Research-Paper-Discovery
## Project Description
The **Multimodal Research Paper Discovery Platform** aims to revolutionize the way researchers discover academic papers by integrating text, image, and metadata search capabilities. Built using the Cornell University arXiv dataset, this platform employs advanced machine learning models to provide rich, context-aware, and multimodal recommendations.

### Key Features
- **Text-Based Search**:
  - Leverages Sentence-BERT and AllenAI-SPECTER embeddings to analyze titles, abstracts, comments, and categories for similarity-based search.
  - Fine-tuned models for domain-specific performance.

- **Image-Based Search**:
  - Extracts and embeds figures/diagrams from PDFs using models like CLIP or BLIP.
  - Enables multimodal queries combining text and image.

- **Metadata Integration**:
  - Filters results based on authors, publication year, categories, and other metadata.
  - Provides personalized recommendations tailored to user profiles.

- **Advanced Retrieval-Augmented Generation (RAG)**:
  - Dynamically retrieves relevant papers using hybrid similarity metrics.
  - Implements cross-modal attention mechanisms for context refinement.

- **Interactive UI**:
  - Built with React, offering an intuitive interface for querying and exploring results.
  - Visualizes related papers with clustering techniques like t-SNE or UMAP.

### Project Goals
1. Build an end-to-end pipeline with:
   - Clean, modular, and PEP8-compliant code.
   - Automated testing and CI/CD pipelines.
   - Scalable and optimized backend with FastAPI.
   - Multimodal search integrating text, images, and metadata.

2. Deliver an industry-grade platform with:
   - Token-based authentication and secure routing.
   - Efficient database design using LanceDB for embedding storage.
   - Deployment-ready architecture with Docker and cloud hosting.

### Tech Stack
- **Backend**: FastAPI
- **Frontend**: React.js
- **Database**: LanceDB
- **ML Models**: Sentence-BERT, AllenAI-SPECTER, CLIP/BLIP
- **Other Tools**: PyMuPDF, pdfplumber, LangChain, HNSW indexing

### Getting Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/multimodal-research-discovery.git
   cd multimodal-research-discovery
   ```

2. **Set Up Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Backend**:
   ```bash
   uvicorn src.api.main:app --reload
   ```

4. **Run the Frontend**:
   ```bash
   cd src/frontend
   npm install
   npm start
   ```

### Contributing
Contributions are welcome! Please open an issue or submit a pull request with your suggestions.

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

### Acknowledgments
- Dataset: Cornell University arXiv dataset
- Sentence-BERT: Hugging Face Transformers
- Image Models: OpenAI CLIP and BLIP
- LanceDB: Embedding storage for fast retrieval
