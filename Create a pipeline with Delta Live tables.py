# Databricks notebook source
# MAGIC %sh
# MAGIC rm -r /dbfs/delta_lab
# MAGIC mkdir /dbfs/delta_lab
# MAGIC wget -O /dbfs/delta_lab/covid_data.csv https://github.com/MicrosoftLearning/mslearn-databricks/raw/main/data/covid_data.csv

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/pipelines/delta_lab/tables"))

# COMMAND ----------

try:    display(dbutils.fs.ls("dbfs:/pipelines/delta_lab/tables"))
except Exception as e:
    print(f"Directory not found: {e}")


# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SHOW TABLES

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM aggregated_covid_data

# COMMAND ----------

