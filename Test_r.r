
library(ggplot2)

data <- data.frame(x = 1:10, y = 2:11)

stacked_bar_plot <- ggplot(data, aes(x = x, y = y, fill = y)) +
  geom_bar(stat = "identity") +
  labs(title = "Stacked Bar Chart",
       x = "X-axis",
       y = "Y-axis")

stacked_bar_plot
