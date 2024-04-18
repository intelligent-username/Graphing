# Random testing of data, graph
library(ggplot2)

data <- data.frame(
  category = rep(c("A", "B", "C"), each = 10),
  x = rep(1:10, times = 3),
  y = c(sample(1:100, 10), sample(1:100, 10), sample(1:100, 10))
)


complex_stacked_bar_plot <- ggplot(data, aes(x = x, y = y, fill = category)) +
  geom_bar(stat = "identity", position = "stack") +
  labs(title = "Complex Stacked Bar Chart",
       subtitle = "A more sophisticated visualization using ggplot2",
       x = "X-axis",
       y = "Y-axis",
       fill = "Category") +
  scale_fill_brewer(palette = "Paired") +
  theme_minimal() +
  theme(text = element_text(size = 14),
        plot.title = element_text(face = "bold"),
        legend.position = "bottom") + 
  facet_wrap(~category) 

complex_stacked_bar_plot