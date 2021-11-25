## NYU-Multicore-Project

This project refers to Aman's [previous project](https://github.com/Aman-Chopra/Performance-Prediction-Multithreaded-Applications).

Overleaf report link: https://www.overleaf.com/7889469115wqfghprbvycq

### Notebooks

1. [Data Preprocess.ipynb](https://github.com/liubai01/Multicore-NYU-2021/blob/master/Data%20Preprocess.ipynb): Include description how we construct the dataset.
2. [Amdahl's law.ipynb](https://github.com/liubai01/Multicore-NYU-2021/blob/master/Amdahl's%20law.ipynb): Visualize Amdahl's law and propose Amdahl's plus law.
3. [Multicore-Final-Project.ipynb](https://github.com/liubai01/Multicore-NYU-2021/blob/master/Multicore-Final-Project.ipynb): Include Amdahl's net to predict multithreading performance.

### Experiment Result

The prediction of optimal thread and speedup.

- For experiment of Amdahl's Net, refer to [Amdahls' Net.ipynb](https://github.com/liubai01/Multicore-NYU-2021/blob/master/Amdahl's%20Net.ipynb).
- For the rest of experiment, refer to [Baselines.ipynb](https://github.com/liubai01/Multicore-NYU-2021/blob/master/Baselines.ipynb).

| Model             | MAE(Thrd.) | MAE(4)       | MAE(8)       | MAE(16)      | MAE(32)      |
| ----------------- | ---------- | ------------ | ------------ | ------------ | ------------ |
| Amdahl's Net      | **8.423**  | 0.667163     | 1.076861     | 1.433249     | 1.939297     |
| Linear Regression | 10.538     | **0.508378** | **0.843289** | 1.362984     | 1.346640     |
| KNN               | 10.692     | 0.624045     | 0.910674     | **1.149755** | **1.154570** |
| Random Forest     | 9.154      | 0.657134     | 1.012102     | 1.278643     | 1.238815     |

**Conclusion**: Amdahl's Net is good at predicting optimal thread but bad at predicting actual speed-up.

