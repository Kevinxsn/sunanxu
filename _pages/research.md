---
layout: page
permalink: /research/
title: Research
description: Algorithms and machine learning for biological discovery.
nav: true
nav_order: 1
---

I build computational methods for reconstructing biological sequences, understanding gene regulation, and evaluating machine learning models. My work brings together algorithm design, biological measurements, and learned representations.

## De novo sequencing of long, highly charged peptides

**Advisor: [Prof. Pavel Pevzner](https://jacobsschool.ucsd.edu/faculty/profile?id=119)**<br>
Computer Science and Engineering, UC San Diego · September 2025–present

The recently proposed two-dimensional partial covariance mass spectrometry generates information about fragment-fragment correlations (FFCs) rather than individual fragment ions like in traditional tandem mass spectrometry. While the FFC approach is foundational to coincidence/covariance spectroscopy—a Nobel Prize-winning technique originating in nuclear physics—until recently, its applications have been limited to very small molecules. However, coincidence/covariance spectroscopy was recently extended to proteomics by introducing a new mode of spectral acquisition that generates FFC maps. FFC maps convert peptide sequencing from inference based on isolated fragment masses into inference based on experimentally observed relationships between fragments. We introduce DeNovoFFC, a computational framework designed to exploit this new information. By applying DeNovoFFC to FFC maps generated using the new capabilities of the Astral mass spectrometer, we demonstrate the feasibility of de novo sequencing of long peptides (>30 amino acids)—a longstanding challenge for peptide sequencing approaches.

<hr>

## Single-cell gene regulatory networks for the adult mouse brain

**Advisor: [Prof. Bing Ren](https://www.nygenome.org/about-us/our-people/senior-leadership/bing-ren-phd/)**<br>
Institute for Genomic Medicine, UC San Diego · January 2024–October 2026

Histone modifications underpin the cell-type-specific gene regulatory programs that drive the remarkable

cellular diversity of the mammalian brain. Here, we jointly profiled four histone modifications and the tran-
scriptome in 2.5 million nuclei from the adult mouse brain. By integrating these data with chromatin acces-
sibility, DNA methylation, and three-dimensional genome organization, we constructed a unified epigenomic

atlas spanning over 100 brain cell subclasses and assigned active, primed, and repressive chromatin
states across 81% of the genome. Active chromatin states marked by combinatorial histone modifications
better nominate candidate enhancers with functional support than chromatin accessibility alone, while
H3K27me3- and H3K9me3-marked chromatin states delineate distinct modes of cell-type-specific gene
repression. Finally, this multimodal resource enables the development of deep learning models that predict

cell-type-specific epigenomic features and gene expression from DNA sequence, providing a comprehen-
sive framework for annotating the brain regulatory genome and interpreting non-coding disease risk variants.

<hr>

## CHEWS improves cis-heritability precision over individual-level GCTA for sparse regulation in small samples

**Advisor: [Prof. Tiffany Amariuta](https://amariutalab.org)**<br>
Halıcıoğlu Data Science Institute, UC San Diego · January 2024–March 2026

We developed CHEWS (Cis-Heritability Estimation With SuSiE), a method for estimating cis-SNP heritability (cis-h²) using fine-mapped genetic effects and summary statistics, without requiring individual-level genotype data. We benchmarked CHEWS against GCTA across 20,294 simulation pairs spanning 350 genomic regions, varying sample size, heritability, genetic architecture, allele frequency, and linkage disequilibrium. We further evaluated both methods using gene expression data from 19,432 genes in GTEx v8 whole blood.

CHEWS demonstrated greater accuracy than GCTA in small samples and sparse genetic architectures, outperforming GCTA at 76% of loci with a single causal variant and achieving lower mean absolute error at n=100 (0.142 vs. 0.205). However, CHEWS tended to underestimate heritability when genetic regulation involved many causal variants, where GCTA remained more reliable. In GTEx, agreement between the methods improved with increasing sample size, with correlation rising from 0.61 to 0.88. These findings highlight CHEWS as a promising alternative for estimating cis-heritability from summary statistics, particularly in small-sample settings with sparse genetic regulation, while emphasizing the importance of selecting estimators based on sample size and underlying genetic architecture.

<hr>

## Data contamination in large language models

**Advisor: [Prof. Jingbo Shang](https://shangjingbo1226.github.io)**<br>
Halıcıoğlu Data Science Institute, UC San Diego · January 2023–September 2025

The opacity in developing large language mod- els (LLMs) is raising growing concerns about the potential contamination of public bench- marks in the pre-training data. Existing contam- ination detection methods are typically based on the text overlap between training and eval- uation data, which can be too superficial to re- flect deeper forms of contamination. In this paper, we first present a cross-lingual form of contamination that inflates LLMs’ perfor- mance while evading current detection meth- ods, deliberately injected by overfitting LLMs on the translated versions of benchmark test sets. Then, we propose generalization-based approaches to unmask such deeply concealed contamination. Specifically, we examine the LLM’s performance change after modifying the original benchmark by replacing the false an- swer choices with correct ones from other ques- tions. Contaminated models can hardly gener- alize to such easier situations, where the false choices can be not even wrong, as all choices are correct in their memorization. Experimen- tal results demonstrate that cross-lingual con- tamination can easily fool existing detection methods, but not ours. In addition, we dis- cuss the potential utilization of cross-lingual contamination in interpreting LLMs’ working mechanisms and in post-training LLMs for en- hanced multilingual capabilities. The code and dataset we use can be obtained from https:// github.com/ShangDataLab/Deep-Contam.

[Read my publications]({{ '/publications/' | relative_url }})
