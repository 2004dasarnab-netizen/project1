library(readxl)
# Read the Excel file
data <- read_excel("C:\\Users\\Arpan_PC\\Downloads\\zone_vs_flat_price_contingency_table.xlsx")

# Convert the data frame into a matrix for the test
# Remove the first column (Zone names) and set it as row names
rownames(data) <- data[[1]]
data_matrix <- as.matrix(data[,-1])

# Perform Pearson's Chi-square test
chisq_test <- chisq.test(data_matrix)

# View the test result
print(chisq_test)
