

#To load a JSON file you can use:
#Below code loads data from json file, convert its format into parquet.
	df = spark.read.load("examples/src/main/resources/people.json", format="json")
	df.select("name", "age").write.save("namesAndAges.parquet", format="parquet")
	


#To load a CSV file:
    df = spark.read.load("examples/src/main/resources/people.csv",
                     format="csv", sep=";", inferSchema="true", header="true")
                     
#Run SQL on files directly
#Instead of using read API to load a file into DataFrame and query it, you can also query that file directly with SQL.

    df = spark.sql("SELECT * FROM parquet.`examples/src/main/resources/users.parquet`")
    
#Saving to Persistent Tables
#DataFrames can also be saved as persistent tables into Hive metastore using the saveAsTable command

#Bucketing, Sorting and Partitioning
#For file-based data source, it is also possible to bucket and sort or partition the output. Bucketing and sorting are applicable only to persistent tables:
    df.write.bucketBy(42, "name").sortBy("age").saveAsTable("people_bucketed")
#while partitioning can be used with both save and saveAsTable when using the Dataset APIs.
    df.write.partitionBy("favorite_color").format("parquet").save("namesPartByColor.parquet")
#It is possible to use both partitioning and bucketing for a single table:    
    df = spark.read.parquet("examples/src/main/resources/users.parquet")
    (df
        .write
        .partitionBy("favorite_color")
        .bucketBy(42, "name")
        .saveAsTable("users_partitioned_bucketed"))
        
###########################################################
#       Ignore Corrupt Files
# enable ignore corrupt files via the data source option
# dir1/file3.json is corrupt from parquet's view
    test_corrupt_df0 = spark.read.option("ignoreCorruptFiles", "true")\
        .parquet("examples/src/main/resources/dir1/",
                 "examples/src/main/resources/dir1/dir2/")
    test_corrupt_df0.show()
# +-------------+
# |         file|
# +-------------+
# |file1.parquet|
# |file2.parquet|
# +-------------+

# enable ignore corrupt files via the configuration
    spark.sql("set spark.sql.files.ignoreCorruptFiles=true")
# dir1/file3.json is corrupt from parquet's view
    test_corrupt_df1 = spark.read.parquet("examples/src/main/resources/dir1/",
                                          "examples/src/main/resources/dir1/dir2/")
    test_corrupt_df1.show()
# +-------------+
# |         file|
# +-------------+
# |file1.parquet|
# |file2.parquet|
# +-------------+


#       Modification Time Path Filters

# Only load files modified before 07/1/2050 @ 08:30:00
    df = spark.read.load("examples/src/main/resources/dir1",
                         format="parquet", modifiedBefore="2050-07-01T08:30:00")
    df.show()
# +-------------+
# |         file|
# +-------------+
# |file1.parquet|
# +-------------+
# Only load files modified after 06/01/2050 @ 08:30:00
    df = spark.read.load("examples/src/main/resources/dir1",
                         format="parquet", modifiedAfter="2050-06-01T08:30:00")
    df.show()
# +-------------+
# |         file|
# +-------------+
# +-------------+