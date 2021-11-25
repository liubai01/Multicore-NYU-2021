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

| Model                  | MAE(Thrd.) | MAE(4)       | MAE(8)       | MAE(16)      | MAE(32)      |
| ---------------------- | ---------- | ------------ | ------------ | ------------ | ------------ |
| Linear Regression      | 8.686      | **0.258448** | **0.711136** | 1.857727     | 1.813439     |
| KNN                    | 8.103      | 0.389432     | 0.829327     | 1.321936     | 1.333033     |
| Random Forest          | 7.159      | 0.431825     | 1.012102     | 1.634928     | 1.534662     |
| Decision Tree          | 7.170      | 0.460841     | 1.390632     | 2.123039     | 2.735234     |
| **Amdahl's Net(Ours)** | **4.692**  | 0.389795     | 0.779149     | **1.243233** | **1.288864** |

**Conclusion**: Amdahl's Net is good at predicting optimal thread but bad at predicting actual speed-up.

