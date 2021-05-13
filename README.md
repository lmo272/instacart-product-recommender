# 🥕 Instacart Product Recommender

## ℹ️ General Information 
The project was part of the 2487-S2 Machine Learning course for the MSc in Business Analytics taught at Nova School of Business and Economics. The topic and scope of the project could be freely chosen by the students, based on given datasets.

### 👨‍💻 Group members
- Frederik Søegaard - 44898
- Lennart Max Oser - 44379
- Niclas Frederic Sturm - 45914

## 💡 About the project
This repository contains the prototype of a product recommender based on data from online grocer [Instacart](https://www.instacart.com/ "Instacart's Homepage"). 

The goal was to first **identify a business problem** faced by e-commerce comapnies such as Instacart, second **explore the avaialble data** to get an understaning of what we can work with and then finally prototype a product recommendation engine based on the products in the basket of a used. In addition to the jupyter notebooks, we also created a **Command Line Interface (CLI)** to play around with our built recommendation engine. On top of that, we also created **an API** to demonstrate how such an engine could be used as a Microservice within a company (i.e. Instacart). 


## 🔎 Files overview

We divided the project in total of 6 parts numbered from `0` to `5`. Additionally, there is a data folder which has to be created following the instructions below. Here you find an overview of the strucure:
```bash
├── 0_Introduction
│   └── 0_Introduction.ipynb
├── 1_Exploratory_Data_Analysis
│   └── 1_exploratory_data_analysis.ipynb
├── 2_Clustering
│   └── 2_clustering.ipynb
├── 3_Item2Vec
│   ├── 3_0_Item2Vec.ipynb
│   └── 3_1_Recommendation_Testing.ipynb
├── 4_Command_Line_Interface
│   ├── CLI_Specification.md
│   └── recommend_me_something.py
├── 5_Recommender_API
│   ├── API_Specification.md
│   ├── engine
│   │   └── recommender_engine.py
│   └── recommender_api.py
├── data
│   ├── aisles.csv
│   ├── departments.csv
│   ├── order_products__prior.csv
│   ├── order_products__train.csv
│   ├── orders.csv
│   ├── products.csv
│   └── sample_submission.csv
├── environment.yml
└── README.md
```

## 💻 Usage
In order to run the code in the same environment as we did please create a virtual environment running the command `conda env create -f environment.yml`. 

After doing so, you should be able to choose the new environment called `instacart` in your preferred IDE.

#### To download the data run the following steps:
1. In your CLI run `mkdir data` or manually create a folder called `data`
2. Run `cd data` in your CLI to get in the right directory
3. Now run the following command to download the data `kaggle competitions download -c instacart-market-basket-analysis`. If you prefer to manually download the data click [here](https://www.kaggle.com/c/instacart-market-basket-analysis/data "Instacart data download)")
4. Extract the zip files using the CLI or what ever method you prefer
