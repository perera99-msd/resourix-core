# ♻️ Resourix Core: AI-Driven Industrial Symbiosis Platform

![Status](https://img.shields.io/badge/Status-Prototype-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Stack](https://img.shields.io/badge/Tech-MERN_%2B_Python-green?style=flat-square)
![Focus](https://img.shields.io/badge/Focus-Circular_Economy-teal?style=flat-square)

## 📄 Abstract
**Resourix** is a B2B SaaS marketplace designed to facilitate the **Circular Economy** within Sri Lanka's manufacturing sector. It addresses critical market inefficiencies in industrial waste exchange through a "Dual-Core" AI architecture:

1.  **Semantic Discovery (NLP):** Utilizes Transformer-based vector embeddings to match vague waste descriptions (e.g., *"Cotton Offcuts"*) with precise raw material needs (e.g., *"Cellulose Filler"*), solving the industry vocabulary mismatch problem.
2.  **Dynamic Valuation (ML):** Deploys **XGBoost** regression models to provide real-time price estimation for waste streams based on location, material category, and market demand signals.

---

## 🚀 Key Features
* **Smart Listing Engine:** Auto-categorization of waste materials using text analysis.
* **AI Price Advisor:** "Smart Broker" feature suggesting optimal listing prices to maximize liquidity.
* **Symbiosis Graph:** Visual mapping of waste-to-resource connections between factories.
* **Secure B2B Messaging:** Integrated chat for negotiating logistics and transfer details.
* **Sustainability Metrics:** Dashboard tracking diverted waste mass (kg) and carbon footprint reduction.

---

## 🏗 System Architecture (Monorepo)
The project follows a scalable **Microservices-Lite** architecture, separating the business logic from the heavy AI computation.

```bash
resourix-core/
├── client/          # Frontend (React.js + Tailwind CSS + Vite)
├── server/          # Backend API (Node.js + Express + JWT Auth)
├── ai-engine/       # AI Microservice (Python + Flask + Scikit-Learn)
├── docs/            # Project Documentation & University Deliverables
└── README.md        # You are here