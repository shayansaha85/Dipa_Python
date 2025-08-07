import pandas as pd  # Import pandas for reading CSV files
import matplotlib.pyplot as plt  # Import matplotlib for plotting and saving images


def csv_to_image(csv_path, image_path):
      df = pd.read_csv(csv_path)  # Read the CSV file into a DataFrame
      # Create a matplotlib figure and axis, set figure size based on columns and rows
      fig, ax = plt.subplots(figsize = (len(df.columns)*2, len(df)*0.5))
      ax.axis('off')  # Hide the axis

      table = ax.table(
            cellText = df.values,  # Table cell values from DataFrame
            colLabels = df.columns,  # Table column labels from DataFrame
            cellLoc = 'center',  # Center align text in cells
            loc = 'center'  # Center the table in the figure
      )

      table.auto_set_font_size(False)  # Disable automatic font size
      table.set_fontsize(11)  # Set font size for table text
      table.scale(1, 1.5)  # Scale the table (width, height)

      plt.savefig(image_path, bbox_inches = 'tight', dpi = 200)  # Save the figure as an image
      plt.close()  # Close the plot to free memory


csv_to_image('output/cityWithTemperature.csv', 'images/cityWithTemperature.png')  # Call the function to convert CSV