

#########################
# Homework- 2nd Week - #
#########################

###############################################
# ÖDEV 1: Fonksiyonlara Özellik Eklemek.
###############################################

# Görev: cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argumanla biçimlendirilebilir olsun.
# Not: Var olan özelliği de argumandan kontrol edilebilir hale getirebilirsiniz.


# Fonksiyona arguman ile biçimlendirilebilen bir özellik eklemek ne demek?
# Örnek olarak aşağıdaki check_df fonksiyonuna argumanla biçimlendirilebilen 2 özellik eklenmiştir.
# Bu özelliler ile tail fonksiyonunun kaç gözlemi göstereceği ve quantile değerlerinin gösterilip gösterilmeyeceği
# fonksiyona özellik olarak girilmiştir ve bu özellikleri kullanıcı argumanlarla biçimlendirebilmektedir.

"""
    Fonksiyona özellikle olarak ratio argümanı eklenmiştir, True seçilirse sınıfların dağılım oranlarını döndürür.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
# df["alone"] = df["alone"].astype("int64")
# df["adult_male"] = df["adult_male"].astype("int64")
df.dtypes
bool_cols = [col for col in df.columns if df[col].dtypes == "bool"]
df[bool_cols] = df[bool_cols].astype("int64")
# df.quantile metodu bool tipi için hata verdiğinden int tipe dönüştürüldü.

# Kategorik değişkenlerde genel resmi görmek için fonksiyon yazalım:

def cat_summary(dataframe, col_name, plot=False, ratio=False):
    print("############### Sınıf Sayısı ####################")
    print(dataframe[col_name].nunique())
    print("############### Sınıf Dağılımları ####################")
    print(pd.DataFrame(dataframe[col_name].value_counts())   )
    if ratio:
        print("#################Sınıf Dağılım Oranları ##########################")
        print(pd.DataFrame({"Variable": col_name,
                            "Ratio": dataframe[col_name].value_counts() / len(dataframe)}))

    if plot:
        print("#####################Plot#####################")
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()


# df.columns
cat_summary(df, "sex")
cat_summary(df, "sex", plot=False,ratio=True)
cat_summary(df, "embarked", plot=True,ratio=True)



###############################################
# ÖDEV 2: Docstring.
###############################################

# Aşağıdaki fonksiyonlara 4 bilgi (uygunsa) barındıran numpy tarzı docstring yazınız.
# (task, params, return, example)
# check_df(), cat_summary()


def check_df(dataframe, head=5):
    """
    Function which shows:
        - quantile : The Basics Statistics
        - shape : The dimension of dataframe.
        - size : Number of elements in the dataframe.
        - type : The data type of each variable.
        - Column Names : The column labels of the DataFrame.
        - Head : The first "n" rows of the DataFrame.
        - Tail : The last "n" rows of the DataFrame.
        - Null Values : Checking if any "NA" Value is into DataFrame

    Parameters
    ----------
    dataframe : dataframe
        Dataframe where the dataset is kept.
    head : int, optional
        The function which is used to get the first "n" rows.

    Returns
    -------

    Examples
    ------
        import pandas as pd
        df = pd.read_csv("titanic.csv")
        print(check_df(df,10))

    """
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Size #####################")
    print(dataframe.size)
    print("##################### Type #####################")
    print(dataframe.dtypes)
    print("############### Column Names ####################")
    print(dataframe.columns)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("################## Null Values ##################")
    print(dataframe.isnull().values.any())
    print("################## Quantiles ##################")
    print(dataframe.quantile(q=[0, 0.05, 0.50, 0.95, 0.99, 1]))

check_df(df)

df.dtypes

help(check_df)
#####################################################################

def cat_summary(dataframe, col_name, plot=False):
    """
    Basic exploration of the categorical values of a dataframe. You will learn:
        - Distinct observations over requested axis.
        - Categorical Variable Classes and Frequencies.
        - Percentage of the number of unique elements in the related Categorical Variable.

    Parameters
    ----------
    dataframe : dataframe
        Dataframe where the dataset is kept.
    col_name : int
        Categorical variable name to be observed.
    plot : bool
        If provided, the code will show the counts of observations in each categorical bin using bars.

    Returns
    -------

    Examples
    ------
        import pandas as pd
        df = pd.read_csv("titanic.csv")
        print(cat_summary(df,"Age",plot=True))
    """
    df.isnull().values.any()
    print("############### Sınıf Sayısı ####################")
    print(dataframe[col_name].nunique())
    print("############### Sınıf Dağılımları ve Oranları ####################")
    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(),
                        "Ratio": dataframe[col_name].value_counts()/len(dataframe)}))
    print("##########################################")
    if plot == True:
        import  seaborn as sns
        import matplotlib.pyplot as plt
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()

# Docstring'e erişmek için:

?cat_summary

# Fonksiyonu çalıştıralım:
cat_summary(df, "sex", plot=True)






