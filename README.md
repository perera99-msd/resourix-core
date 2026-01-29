# Resourix Core: AI-Driven Industrial Symbiosis Platform

![Status](https://img.shields.io/badge/Status-Prototype-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Stack](https://img.shields.io/badge/Tech-MERN_%2B_Python-green?style=flat-square)

## 📄 Abstract
**Resourix** is a B2B SaaS marketplace designed to optimize the **Circular Economy** in Sri Lanka's manufacturing sector. It addresses critical market failures in industrial waste exchange through a "Dual-Core" AI architecture:

1.  **Semantic Discovery (NLP):** Utilizes Transformer-based vector embeddings to match vague waste descriptions (e.g., "Cotton Offcuts") with precise raw material needs.
2.  **Dynamic Valuation (ML):** Deploys XGBoost regression models to predict real-time market value for waste streams based on location and demand.

## 🏗 System Architecture
The project follows a scalable Microservices-Lite architecture:

* **`client/`**: **React.js (Vite)** frontend with Tailwind CSS.
* **`server/`**: **Node.js & Express** REST API handling auth and marketplace logic.
* **`ai-engine/`**: **Python (Flask)** microservice hosting the AI inference models.
* **Database**: **MongoDB Atlas** (NoSQL).

## 🗓 Project Roadmap
- [ ] **Phase 1:** Synthetic Data Generation & Schema Design
- [ ] **Phase 2:** Marketplace MVP (Auth, Listings, Search)
- [ ] **Phase 3:** Integration of Semantic Matching (NLP)
- [ ] **Phase 4:** Integration of Price Prediction AI

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
