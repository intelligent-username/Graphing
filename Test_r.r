library(ggplot2)

# Create a more complex dataset with a categorical variable
data <- data.frame(
  category = rep(c("A", "B", "C"), each = 10),
  x = rep(1:10, times = 3),
  y = c(sample(1:100, 10), sample(1:100, 10), sample(1:100, 10))
)

# Create a stacked bar plot with additional features
complex_stacked_bar_plot <- ggplot(data, aes(x = x, y = y, fill = category)) +
  geom_bar(stat = "identity", position = "stack") +
  labs(title = "Complex Stacked Bar Chart",
       subtitle = "A more sophisticated visualization using ggplot2",
       x = "X-axis",
       y = "Y-axis",
       fill = "Category") +
  scale_fill_brewer(palette = "Paired") + # Use a color palette for the fill
  theme_minimal() + # Use a minimal theme
  theme(text = element_text(size = 12), # Customize text size
        plot.title = element_text(face = "bold"), # Bold plot title
        legend.position = "bottom") + # Move legend to the bottom
  facet_wrap(~category) # Facet by category

# Display the plot
complex_stacked_bar_plot