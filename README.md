# Gonzalo Díaz Amor

**Senior Data Scientist — LLM Evaluation & Statistical/Causal ML · Healthcare & Pharma**

Data Scientist with 6 years across pharma, healthtech and mobility, and a BSc in Statistics. I work on LLM evaluation (LLM-as-a-Judge, RAG) and statistical/causal ML: pre-registered protocols, confidence intervals on every number, and null results reported as such.

Based in Spain (CET), working remotely.

---

### Featured Projects
* **[llm-judge-stats](https://github.com/gondiam/llm-judge-stats):** Open-source Python package with the statistics to check whether an LLM judge can be trusted: kappa, ICC, bootstrap CIs, sample-size planning and position-bias checks. On the public MT-Bench human judgments (1,814 items), GPT-4 vs. human-majority kappa = 0.51 (95% CI 0.47-0.54), on par with the human-human kappa of 0.50.
* **[sft-dpo-eval](https://github.com/gondiam/sft-dpo-eval):** Pre-registered post-training study on PubMedQA. SFT lifted Qwen3-1.7B from 38.6% to 71.7% (+33.1 points, 95% CI 27.4-38.9); DPO added no gain and is reported as a null result.

* **[bayesian-judge-calibration](https://github.com/gondiam/bayesian-judge-calibration)** (proof of concept): estimating a judge-measured rate from 20 to 200 human labels on MT-Bench. A Bayesian model had the lowest error at every size (RMSE 0.067 vs. 0.110 from the human labels alone at 20 labels).
---

### Professional Highlights
* **LLM evaluation:** Designed an LLM-as-a-Judge for decision audits with per-replica shuffling against position bias and 5-replica majority voting: 91.7% unanimous verdicts over 1,272 comparisons.
* **Pre-registered RAG evaluation:** Confirmatory vs. exploratory hypotheses, power analysis, bootstrap CIs and Benjamini-Hochberg, with failed hypotheses reported without post-hoc threshold changes.
* **Causal ML:** Led the discovery phase of a Causal AI engagement on ~100,000 patients with Double ML and Causal Forest.
* **Clinical data science:** Programming lead for a Phase IV study (SDTM, ADaM); propensity-score-matched real-world evidence on 20,000 patients; OMOP-CDM data lake across 3 hospitals.
* **Engineering:** FastAPI inference APIs, Docker, Airflow, AWS and GCP.

### Technical Stack
* **LLM evaluation & statistics:** LLM-as-a-Judge, pre-registered protocols, power analysis, bootstrap CIs, inter-rater agreement (Cohen's kappa, ICC), Benjamini-Hochberg.
* **GenAI & LLMs:** RAG, hybrid retrieval (dense + BM25, RRF), multi-agent pipelines, LangChain, ChromaDB, fine-tuning (SFT, DPO, LoRA).
* **Languages & ML:** Python, R, SQL, SAS, PyTorch, Scikit-Learn, Causal ML, survival analysis.
* **MLOps & data:** Docker, Airflow, AWS, GCP, CI/CD, PostgreSQL, MySQL, MongoDB.
* **Clinical data standards:** CDISC (SDTM, ADaM), OMOP-CDM (OHDSI).

---

### Education & Certifications
* **MSc Big Data & Data Science** – VIU (2025)
* **BSc Statistics** – UVa, Valladolid (2020)
* **Certifications:** AI Agents Intensive Course (Google x Kaggle, 2025), 6.86x Machine Learning with Python (MITx, 2021)

---

### Contact
* **Email:** [gdiazamor.ds@gmail.com](mailto:gdiazamor.ds@gmail.com)
* **LinkedIn:** [linkedin.com/in/gdiazamor](https://www.linkedin.com/in/gdiazamor)
* **Portfolio:** [gondiam.github.io/Gonzalo_Portfolio](https://gondiam.github.io/Gonzalo_Portfolio/)
* **CV:** [PDF](https://github.com/gondiam/cv/raw/main/output/CV_Gonzalo_DiazAmor_EN.pdf)
