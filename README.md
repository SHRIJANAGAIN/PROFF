# 🚀 Project Surya: SKT OMNI SUPREME (1.1T MoE)
![Model Type](https://img.shields.io/badge/Model-1.1T_MoE-blue?style=for-the-badge&logo=ai&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-ST--X_Extreme-red?style=for-the-badge&logo=rocket&logoColor=white)
![Tokens](https://img.shields.io/badge/Tokens-146_Trillion-orange?style=for-the-badge&logo=data-matrix&logoColor=white)



### **Official Technical Report & Architectural Documentation (v1.0.6)**
​Project Surya is a frontier-scale initiative by SKT AI LABS to develop the world’s most efficient and linguistically capable Mixture-of-Experts (MoE) architecture. Our flagship model, SKT OMNI SUPREME, is a 1.1-Trillion parameter powerhouse trained from scratch on 146 Trillion multi-modal tokens.
​This repository contains the Technical Whitepaper (v1.0.6), architectural configurations, and benchmark logs for public audit and research transparency

[📄 Read the Full Technical Whitepaper (supreme.pdf)](./Supreme.pdf)

**Project Surya** is a frontier-scale research initiative by **SKT AI LABS** focused on scaling Mixture-of-Experts (MoE) architectures to 1.1-Trillion parameters. Our mission is to provide state-of-the-art (SOTA) intelligence for the Global South, with a primary focus on Hinglish, Indian context, and advanced coding reasoning.

---

## 1. Abstract
Hum **SKT OMNI SUPREME** launch kar rahe hain — ek fully from-scratch **1.1 Trillion parameter MoE** foundational model. Yeh model **146 Trillion** high-quality multi-modal tokens par pre-trained hai. Hamara custom **ST-X (Surya Throughput eXtreme)** framework distributed clusters par throughput ko maximize karta hai.

## 2. Architecture & ST-X Framework
The model utilizes a modular Transformer backbone with custom MoE routing enhancements:

| Parameter | Configuration | Technical Rationale |
| :--- | :--- | :--- |
| **Total Parameters** | 1.1T | Deep knowledge compression frontier |
| **Activated Params** | ~165B | Efficient top-2 gating for low-latency |
| **Layers** | 80 | Stability via SwiGLU + RMSNorm |
| **Hidden Dimension** | 8192 | High-dim latents for complex reasoning |
| **Total Experts** | 128 MoE | Balanced workload across 2400 GPU cluster |
| **Context Window** | 512K | FlashAttention-3 + RoPE extensions |
| **Precision** | Mixed | FP8 Weights / BF16 Compute |

## 3. Training Data & Throughput Scaling (The 146T Math)
We utilize **Staged Context Scaling** to maximize compute utilization across the 104-day training window:

* **Phase 1 (0-60T Tokens):** 8k context window → **~9,200 tokens/sec/GPU**.
* **Phase 2 (60-120T Tokens):** 32k-64k context → **~5,500 tokens/sec/GPU**.
* **Final Annealing (120-146T Tokens):** 512k context → **~4,100 tokens/sec/GPU**.

> **Technical Note:** The throughput reported is a weighted average. Early-stage acceleration on shorter sequences enabled the processing of the full 146T token corpus.

| Category | % Mix | Key Sources |
| :--- | :--- | :--- |
| **Code & Logic** | 30% | GitHub, StackOverflow, Synthetic CoT |
| **Scientific/Tech**| 25% | arXiv, PubMed, Indian/Global Legal Docs |
| **Multi-lingual** | 20% | **ShORT-Hinglish 12M**, Hindi, IndicGLUE |
| **Reasoning** | 10% | MATH, GSM8K-hard, GPQA chains |
| **General Web** | 15% | Filtered Common Crawl (RefinedWeb) |

## 4. Benchmarks (March 2026 Internal Eval)
Comparison against frontier-class models (0-shot/few-shot):

| Benchmark | OMNI SUPREME | Comparison (Frontier '26) | Notes |
| :--- | :--- | :--- | :--- |
| **MMLU (English)** | **88.7%** | GPT-5.x ~92% | Strong general knowledge |
| **HumanEval+** | **92.1%** | Claude 4.x ~94% | Top-tier coding |
| **IndicMMLU** | **81.4%** | Sarvam 105B ~78% | **SOTA for Indian Context** |
| **GSM8K-hard** | **95.3%** | Gemini 3.1 ~96% | Logical Chain-of-Thought |

## 5. Challenges & Lessons Learned
* **Router Collapse:** Resolved at 40T tokens via higher auxiliary z-loss.
* **Bhopal Thermal Scaling:** Custom liquid cooling implemented for 2,400 GPU cluster.
* **Quantization Drift:** Mitigated FP8 drift using periodic BF16 master weights.

## 6. Conclusion & Roadmap
* **Vision Integration:** LLaVA-style training on 20B image-text pairs (In Progress).
* **Safety Tuning:** RLAIF and Constitutional AI alignment (Q2 2026).
* **API Access:** Real-time inference beta via custom engine.

---

### 🏛 Citation
```bibtex
@techreport{skt_surya_2026,
  author = {L.K. Tiwari},
  title = {Project Surya: Scaling 1.1T Frontier Intelligence},
  institution = {SKT AI LABS},
  year = {2026},
  version = {1.0.6}
}
